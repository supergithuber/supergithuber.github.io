## 修改HTTP请求头

之前自己做过一个项目，用charles抓包去获取“网易考拉海购”的后台json数据，做一个和它一模一样的APP。

发现通过charles去获取到相应页面的json数据地址的时候，把这个地址配置到我的项目中去，一直崩溃。

在获取的completionHandler中是可以拿到NSData数据的，仔细观察发现项目中获取的json数据和charles看到的json居然有细微的不同

通过软件paw(一款非常便捷查看网页数据，并可以修改请求头的软件)发现：手机访问的请求头和xcode中访问的请求头是不一样的

所以只有在xcode中修改访问的请求头才行，通过国外一个网站搜索到最新的修改方法，其实也蛮简单，但是国内就是找不到，这里记录下：


```objc
// 声明一个请求头字典
NSDictionary *configDictionary = @{
                                       @"Content-Type": @"application/json;charset=UTF-8",
                                       @"User-Agent": @"HTSpring/3.0.0 6565(iPhone; iOS 9.3.2; Scale/2.00)",
                                       @"deviceModel": @"iPhone8,4",
                                       @"appVersion":@"3.0.0",
                                       @"platform":@"2",
                                       @"apiVersion":@"200",
                                       };
//依据你要访问的URL生成一个请求，并修改请求方式和请求头
NSURL *requestUrl = [NSURL URLWithString:urlString];
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:requestUrl];
request.HTTPMethod = @"get";
request.allHTTPHeaderFields = configDictionary;
//开始获取数据
NSURLSession *session = [NSURLSession sharedSession];
NSURLSessionDataTask *dataTask;
dataTask = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error){

//在回调的block中可以拿到获取数据data
}];
//别忘了这才是真正的开始
[dataTask resume];

```



修改userAgent来欺骗后台，然他以为我们是手机访问，

deviceModel就是iphone的型号，

appVersion是网易考拉这个app的版本，

platform等于2代表是ios，如果是1就是安卓，这是他们自己后台定义的，

apiVersion就是他们后台api的版本号，

以上这些我是通过charles看到请求头后，按照给出的来改的，你们可以按照自己的需求修改字典，就可以了。