## info.plist 中的配置

### 1. 和itunes文件共享

UIFileSharingEnabled输入为key，后会变为Application supports iTunes file sharing，把值改为YES

这样当用户把手机插入到电脑后，可以通过iTunes对app沙盒内的文件进行添加和删除

### 2. 授权登录跳转到第三方应用分享

LSApplicationQueriesSchemes是一个数组，添加了以后，在调用canOpenURL时才可以返回YES，进而进行跳转

也可以通过canOpenURL判断是否安装了对应的APP

```
<key>LSApplicationQueriesSchemes</key>
<array>
    <!-- 微信 URL Scheme 白名单-->
    <string>wechat</string>
    <string>weixin</string>

    <!-- 新浪微博 URL Scheme 白名单-->
    <string>sinaweibohd</string>
    <string>sinaweibo</string>
    <string>sinaweibosso</string>
    <string>weibosdk</string>
    <string>weibosdk2.5</string>

    <!-- QQ、Qzone URL Scheme 白名单-->
    <string>mqqapi</string>
    <string>mqq</string>
    <string>mqqOpensdkSSoLogin</string>
    <string>mqqconnect</string>
    <string>mqqopensdkdataline</string>
    <string>mqqopensdkgrouptribeshare</string>
    <string>mqqopensdkfriend</string>
    <string>mqqopensdkapi</string>
    <string>mqqopensdkapiV2</string>
    <string>mqqopensdkapiV3</string>
    <string>mqqopensdkapiV4</string>
    <string>mqzoneopensdk</string>
    <string>wtloginmqq</string>
    <string>wtloginmqq2</string>
    <string>mqqwpa</string>
    <string>mqzone</string>
    <string>mqzonev2</string>
    <string>mqzoneshare</string>
    <string>wtloginqzone</string>
    <string>mqzonewx</string>
    <string>mqzoneopensdkapiV2</string>
    <string>mqzoneopensdkapi19</string>
    <string>mqzoneopensdkapi</string>
    <string>mqqbrowser</string>
    <string>mttbrowser</string>

    <!-- 支付宝 URL Scheme 白名单-->
    <string>alipay</string>
    <string>alipayshare</string>

    <!-- 人人 URL Scheme 白名单-->
    <string>renrenios</string>
    <string>renrenapi</string>
    <string>renren</string>
    <string>renreniphone</string>

    <!-- 来往 URL Scheme 白名单-->
    <string>laiwangsso</string>

    <!-- 易信 URL Scheme 白名单-->
    <string>yixin</string>
    <string>yixinopenapi</string>

    <!-- instagram URL Scheme 白名单-->
    <string>instagram</string>

    <!-- whatsapp URL Scheme 白名单-->
    <string>whatsapp</string>

    <!-- line URL Scheme 白名单-->
    <string>line</string>

    <!-- Facebook URL Scheme 白名单-->
    <string>fbapi</string>
    <string>fb-messenger-api</string>
    <string>fbauth2</string>
    <string>fbshareextension</string>

    <!-- Kakao URL Scheme 白名单-->  
    <!-- 注：以下第一个参数需替换为自己的kakao appkey--> 
    <!-- 格式为 kakao + "kakao appkey"-->    
    <string>kakaofa63a0b2356e923f3edd6512d531f546</string>
    <string>kakaokompassauth</string>
    <string>storykompassauth</string>
    <string>kakaolink</string>
    <string>kakaotalk-4.5.0</string>
    <string>kakaostory-2.9.0</string>

   <!-- pinterest URL Scheme 白名单-->  
    <string>pinterestsdk.v1</string>
</array>
```

### 3. 和外设交互

UISupportedExternalAccessoryProtocols，一个数组，声明协议的名称，这样在插入具有相关协议的外设后，才可以启动相应的APP。

项目中还需要导入ExternalAccessory.framework框架

### 4. 默认语言

Localization native development region，xcode建立工程的时候，默认语言是英文，所以有些APP调用系统相机或者相册之类的东西，默认语言是英文。

把这个修改为China，这样打开的就是中文显示

### 5. 请求权限弹框提示语

```
Privacy - Microphone Usage Description //麦克风权限
Privacy - Contacts Usage Description   //通讯录权限
Privacy - Camera Usage Description     //摄像头权限
Privacy - NSSiriUsageDescription       //Siri的权限
Privacy - Bluetooth Peripheral Usage Description //蓝牙
Privacy - Reminders Usage Description  //提醒事项
Privacy - Motion Usage Description     //运动与健康
Privacy - Media Libaray Usage Description //媒体资源库
Privacy - Calendars Usage Description  //日历
```
### 6. 在特定的设备上才可以运行

Required device capabilities，一个数组

armv7，只有这个架构CPU的设备才可以运行
wifi，只有具有wifi功能的设备才可以运行
telephone，只有可以挂电话的设备才可以运行
microphone，只有具有麦克风的设备才可以运行

模拟器:
4s-5: i386

5s-6s Plus: x86_64

真机(iOS设备):
armv6: iPhone、iPhone 2、iPhone 3G、iPod Touch(第一代)、iPod Touch(第二代)

armv7: iPhone 3Gs、iPhone 4、iPhone 4s、iPad、iPad 2

armv7s: iPhone 5、iPhone 5c (静态库只要支持了armv7,就可以在armv7s的架构上运行)

arm64(注:无armv64): iPhone 5s、iPhone 6、iPhone 6 Plus、iPhone 6s、iPhone 6s Plus、iPad Air、iPad Air2、iPad mini2、iPad mini3

### 7. 只能在iphone上运行，不可以在iPad或者touch上运行

Application requires iPhone environment设为YES