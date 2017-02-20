## oc和Swift混合编译

  今天第一次接触oc和swift混合编译的项目，总结一下它们之间相互调用的方式。
  
### objective-C调用swift
当你在objective-C的项目中新建一个swift文件的时候，Xcode会自动为项目生成头文件来提供给objective-C调用。你只需要在调用的地方#import  "productName-Swift.h"即可，其中productName指的是工程的名字。
这个文件是无法搜到的，只能在import后，通过 commond+单击 查看到

### swift调用objective-C
当你在oc项目中新建swift文件，或者是在swift项目中新建oc文件时，Xcode都会为你新建一个桥接文件，文件名为procuctName-bridging-Header.h，其中productName为工程名称，你当然也可以在如图所示的配置中修改默认桥接文件，指定为自己创建的文件

![ocMixSwift_1](https://supergithuber.github.io/img/ocMixSwift_1.png)

如下图所示，在其中import需要给swift调用的oc类的头文件，Xcode会帮你生成对应的swift风格接口

![ocMixSwift_2](https://supergithuber.github.io/img/ocMixSwift_2.png)

选中objective-C的头文件，通过点击Related Items按钮，选择其中的Generated Interface可以看到Xcode为我们生成的Swift风格的接口

![ocMixSwift_3](https://supergithuber.github.io/img/ocMixSwift_3.png)