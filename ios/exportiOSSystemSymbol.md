## 从iOS固件ipsw中提取系统符号表

提取系统的符号表一般从iOS真机中获取，但是有一些情况难以获取到对应系统的真机。

例如：iOS10.3.4的发布时间是2019年7月23日，iOS10.3.3的发布时间是2017年7月19日，中间间隔了两年的时间。在2020年，如果要获取iOS10.3.3的真机实在是太难了，因为官方只支持升级到最新系统。

> iOS系统历史版本以及发布时间可参考[wiki](https://zh.wikipedia.org/wiki/IOS版本历史)

这个时候就要用其他的方法获取到系统符号表。例如从ipsw固件中获取。

#### 准备

1. 去一些固件下载网站[theiphonewiki.com](https://www.theiphonewiki.com/wiki/Firmware)下载对应版本的固件
2. 下载dmg解密工具，VFDecrypt命令行或者是它的客户端iDecrypt等能够解密dmg的工具，不好找。此处提供一个[iDecrypt](https://supergithuber.github.io/Resources/iDecrypt-Mac-build91-bennyyboi.zip)