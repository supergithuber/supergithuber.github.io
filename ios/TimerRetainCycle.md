# Timer retainCycle In Swift 


在ios中，当一个controller weak持有一个timer，timer初始化的时候调用（objective-C有类似方法）

```
self.timer = Timer.scheduledTimer(timeInterval: interval, target:self, selector: #selector(someFunction), userInfo: nil, repeats: true)
```

的时候，就一定会发生循环引用（不知道为何这里的weak就无效了），此时我目前想到有两种解决方案

#### 1. 在viewWillDisappear或者是viewDidDisappear中

```
self.timer.invalidate()
self.timer = nil
```

#### 2. 在controller内定义一个私有内部类，这个类的作用就是提供一个外部类对象，生成一个weak的内部类对象，并提供一个方法调用外部类的周期函数

此处的外部类名叫：BluetoothViewController

```
	private class TimerTargetWrapper {
        weak var interactor:BluetoothViewController?
        init(interactor: BluetoothViewController) {
            self.interactor = interactor
        }
        
        @objc func timerFunction(timer: Timer?){
            interactor?.rescanCamera()
        }
    }
```

然后就可以在外部类中这么调用，避免循环引用

```
let weakSelf = TimerTargetWrapper.init(interactor: self)
self.scanTimer = Timer.scheduledTimer(timeInterval: 3, target:weakSelf, selector: #selector(weakSelf.timerFunction(timer:)), userInfo: nil, repeats: true)
```