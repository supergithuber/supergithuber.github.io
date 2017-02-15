## 合成视频中间掉帧的问题

有一个需求需要把两段视频合成成一段，在苹果官网上找到一个合成方式[Putting It All Together: Combining Multiple Assets and Saving the Result to the Camera Roll](https://developer.apple.com/library/prerelease/content/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/03_Editing.html)，自己按照文档去实现了它，发现一个很严重的问题，中间出现掉帧的黑帧问题，想不到苹果爸爸也会出现这个问题。找了下出现问题的原因，发现有几个重大问题：

1. 不准确的参数，没有给提取AVURLAsset对象的提取参数中配置精确的时间，需要给它的AVURLAssetPreferPreciseDurationAndTimingKey属性设置为YES
2. 没有给AVAssetExportSession的videoComposition属性配置合适的参数，这些参数应该来自于实际的视频
3. 应该在videoComposition属性的instructions字典属性中严格配置来自视频的音视频轨道信息
4. 切记提取视频的时间信息的时候要使用asset.timerange.duration来获取

下面给出完整的函数代码，已经成功采用在我的项目[LivePhoto-Demo](https://github.com/supergithuber/LivePhoto-Demo)中，可以直接使用:


```objc
+ (void)mergeVideoFiles:(NSMutableArray *)fileURLs
             completion:(void(^)(AVAssetExportSession * exportor))completion {
    //起始没有第一段视频
    AVAsset *firstAsset = [AVURLAsset assetWithURL:(NSURL *)fileURLs.firstObject];
    if (![firstAsset tracksWithMediaType:AVMediaTypeVideo].firstObject)
    {
        [fileURLs removeObjectAtIndex:0];
    }

    AVMutableComposition *composition = [[AVMutableComposition alloc] init];
    AVMutableCompositionTrack *videoTrack = [composition addMutableTrackWithMediaType:AVMediaTypeVideo
                                                                     preferredTrackID:kCMPersistentTrackID_Invalid];
    AVMutableCompositionTrack *audioTrack = [composition addMutableTrackWithMediaType:AVMediaTypeAudio
                                                                     preferredTrackID:kCMPersistentTrackID_Invalid];
    NSMutableArray *instructions = [NSMutableArray new];
    
    __block CMTime currentTime = kCMTimeZero;
    __block CGSize size = CGSizeZero;
    __block int32_t highestFrameRate = 0;
    
    [fileURLs enumerateObjectsUsingBlock:^(NSURL *fileURL, NSUInteger idx, BOOL *stop) {
#pragma unused(idx)
        
        NSDictionary *options = @{AVURLAssetPreferPreciseDurationAndTimingKey:@YES};
        AVURLAsset *sourceAsset = [AVURLAsset URLAssetWithURL:fileURL options:options];
        AVAssetTrack *videoAsset = [[sourceAsset tracksWithMediaType:AVMediaTypeVideo] firstObject];
        AVAssetTrack *audioAsset = [[sourceAsset tracksWithMediaType:AVMediaTypeAudio] firstObject];
        if (CGSizeEqualToSize(size, CGSizeZero)) { size = videoAsset.naturalSize; }
        
        int32_t currentFrameRate = (int)roundf(videoAsset.nominalFrameRate);
        highestFrameRate = (currentFrameRate > highestFrameRate) ? currentFrameRate : highestFrameRate;
        

        CMTime trimmingTime = CMTimeMake(lround(videoAsset.naturalTimeScale / videoAsset.nominalFrameRate), videoAsset.naturalTimeScale);
        CMTimeRange timeRange = CMTimeRangeMake(trimmingTime, CMTimeSubtract(videoAsset.timeRange.duration, trimmingTime));
        
        NSError *videoError;
        [videoTrack insertTimeRange:timeRange ofTrack:videoAsset atTime:currentTime error:&videoError];
        
        NSError *audioError;
        [audioTrack insertTimeRange:timeRange ofTrack:audioAsset atTime:currentTime error:&audioError];
        
            AVMutableVideoCompositionInstruction *videoCompositionInstruction = [AVMutableVideoCompositionInstruction videoCompositionInstruction];
            videoCompositionInstruction.timeRange = CMTimeRangeMake(currentTime, timeRange.duration);
            videoCompositionInstruction.layerInstructions = @[[AVMutableVideoCompositionLayerInstruction videoCompositionLayerInstructionWithAssetTrack:videoTrack]];
            [instructions addObject:videoCompositionInstruction];
            
            currentTime = CMTimeAdd(currentTime, timeRange.duration);
        
    }];
    
    AVAssetExportSession *exportSession = [[AVAssetExportSession alloc] initWithAsset:composition presetName:AVAssetExportPresetHighestQuality];
    unlink([MTLivePhotoMergeVideoPath UTF8String]);
    exportSession.outputURL = [NSURL fileURLWithPath:MTLivePhotoMergeVideoPath];
    exportSession.outputFileType = AVFileTypeMPEG4;
    exportSession.shouldOptimizeForNetworkUse = YES;
    
    AVMutableVideoComposition *mutableVideoComposition = [AVMutableVideoComposition videoComposition];
    mutableVideoComposition.instructions = instructions;
    mutableVideoComposition.frameDuration = CMTimeMake(1, highestFrameRate);
    mutableVideoComposition.renderSize = size;
    exportSession.videoComposition = mutableVideoComposition;
    
    
    [exportSession exportAsynchronouslyWithCompletionHandler:^{
        dispatch_async(dispatch_get_main_queue(), ^{
            if (completion) {
                completion(exportSession);
            }
        });
        
    }];

}
```

