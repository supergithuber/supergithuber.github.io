## Autolayout和Layer

iOS中UIView是支持autolayout的，但是CALayer是不支持的。经常我们又会使用Massory（objective-C），Snapkit（swift）一些自动布局框架。

但是一些layer的布局又依赖于他的父layer，我们无法在autolayout之前知道view的layer宽高，确切知道的时机又不好确定。例如一些gradientlayer加到view的layer上。

#### 1. 在controller的viewDidLayoutSubviews

在controller的viewDidLayoutSubviews方法内，view的frame和它的layer的大小都是确定的，因此可以在这个方法内部对layer设置它的frame。

```objective-c
- (void)viewDidLayoutSubviews { 
    [super viewDidLayoutSubviews]; 

    [self.testLabel sizeToFit]; 
    self.testLabel.center = self.view.center; 

    self.gradientLayer.cornerRadius = self.testLabel.frame.size.height/2; 
    CGFloat margin = 10;//gradientLayer左右需要有边距 
    CGRect frame = self.testLabel.frame; 
    frame.origin.x -= margin; 
    frame.size.width += margin*2; 
    self.gradientLayer.frame = frame; 
}
```

这么做的缺点就是代码分散，不好管理

#### 2. 重写view的+ (Class)layerClass方法

每个UIView底层都有一个CALayer，并且UIView有一个API+ (Class)layerClass，允许我们自定义CALayer的类。那我们就可以自定义一个UILabel，重写+ (Class)layerClass方法返回CAGradientLayer。我们只需要对UILabel进行约束，就会映射到它自身的CALayer。

```objective-c
@implementation CustomLabel 
+ (Class)layerClass { 
    return [CAGradientLayer class]; 
} 

- (void)layoutSubviews { 
    [super layoutSubviews]; 

    CAGradientLayer *gradientLayer = (CAGradientLayer *)self.layer; 
    gradientLayer.colors = @[(id)[[UIColor alloc] initWithRed:16/255.0 green:175/255.0 blue:211/255.0 alpha:1].CGColor, (id)[[UIColor alloc] initWithRed:33/255.0 green:94/255.0 blue:147/255.0 alpha:1].CGColor]; 
    gradientLayer.locations = @[@(0), @(1)]; 
    gradientLayer.startPoint = CGPointMake(0, 0); 
    gradientLayer.endPoint = CGPointMake(1, 0); 
    self.layer.cornerRadius = self.bounds.size.height/2.0; 
} 
@end
```

优点：只要封装好UILabel，有类似的需求，直接拿来用就是了。
缺点：就是因为使用前要自定义一个类，不可能对所有类似要求的控件子类化。有时候只是一个小需求，就要自定义一个view


#### 3. 通过方法交换，把view的layoutSubviews方法回调出来

这个方法类似上面一个方法的变种，减少代码分散，较少额外的代码

新建一个分类

```objevtive-c

@interface UIView (LayoutSubviewsCallback)


@property (nonatomic, copy)void (^layoutSubviewsCallback)(UIView *);

@end

@implementation UIView (LayoutSubviewsCallback) 

+ (void)load { 
    Method originalMethod = class_getInstanceMethod(self, @selector(layoutSubviews)); 
    Method newMethod = class_getInstanceMethod(self, @selector(jx_layoutSubviews));
    method_exchangeImplementations(originalMethod, newMethod); 
} 

- (void)jx_layoutSubviews { 
    [self jx_layoutSubviews]; 
    !self.layoutSubviewsCallback ?: self.layoutSubviewsCallback(self); 
} 

- (void)setLayoutSubviewsCallback:(void (^)(UIView *))layoutSubviewsCallback {
    objc_setAssociatedObject(self, "layoutSubviewsCallback", layoutSubviewsCallback, OBJC_ASSOCIATION_RETAIN); 
} 

- (void (^)(UIView *))layoutSubviewsCallback { 
    return objc_getAssociatedObject(self, "layoutSubviewsCallback"); 
} 

@end
```

在外部使用的时候，就可以

```objective-c
    CAGradientLayer *gradientLayer = [CAGradientLayer layer]; 
    gradientLayer.colors = @[(id)[[UIColor alloc] initWithRed:16/255.0 green:175/255.0 blue:211/255.0 alpha:1].CGColor, (id)[[UIColor alloc] initWithRed:33/255.0 green:94/255.0 blue:147/255.0 alpha:1].CGColor]; 
    gradientLayer.locations = @[@(0), @(1)]; 
    gradientLayer.startPoint = CGPointMake(0, 0); 
    gradientLayer.endPoint = CGPointMake(1, 0); 
    [self.view.layer addSublayer:gradientLayer]; 
    self.testLabel.layoutSubviewsCallback = ^(UIView *view) { 
        gradientLayer.frame = view.frame; 
        gradientLayer.cornerRadius = view.bounds.size.height/2.0; 
    };
```