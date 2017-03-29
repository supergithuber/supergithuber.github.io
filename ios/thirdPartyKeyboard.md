## 第三方键盘内容方向错误

在使用第三方键盘的时候，遇到一个少见的坑：在屏幕是方向是upsidedown的时候，当设备方向为landscapeLeft或者是landScapeRight，键盘的弹出方向是正确的，但是键盘的内容方却是横屏的，也就是说太宽了，超出了屏幕范围。

这个问题也只有第三方键盘会出现，系统的键盘是正常的。原因是：

1. 系统键盘的弹出方向和内容方向都是取决于屏幕方向
2. 第三方键盘的弹出方向取决于屏幕方向，但是内容方向却取决于设备方向和屏幕方向两者，而第三方键盘***不支持***当屏幕方向为upsidedown的时候，设备方向为水平的情况

为了解决这个bug，过程中尝试了通过监听键盘弹出通知、或者是键盘frame改变通知来修改frame的方法，无法奏效。

最终通过在键盘弹出通知的函数中修改设备方向，让设备方向为portrait来解决这个问题

```objc
[[UIDevice currentDevice] setValue:[NSNumber numberWithInt: UIInterfaceOrientationPortrait] forKey:@"orientation"]
```