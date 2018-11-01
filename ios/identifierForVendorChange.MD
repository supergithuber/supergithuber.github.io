## identifierForVendor会改变的情况

（identifierForVendor）UIDevice.current.identifierForVendor 

（advertisingIdentifier ）NSString *adId = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];


| 情况  |  是否会变化   |
| -----  | ---------  |
|在iOS的设置应用中选择“重置所有设置” | 不会 |
|在iOS的设置应用中“清除所有的内容和设置” | 会   |
| 通过iTunes还原设备  | 会   |
|从设备上删除该APP  | 如果该APP是某个开发者账号下在该设备上的最后一个APP时，会影响identifierForVendor 的值，否则不会影响该字段的值 |
| 升级应用  | 不会  |
|启用或关闭“限制广告追踪” | 会影响advertisingIdentifier  |
| 系统升级（通过手机自己升级或通过iTunes升级） | 会  |
| 在iOS的设置应用中“重新设置广告标示符” | 会改变advertisingIdentifier 的值。如果一些应用正在请求该字段，那么在该应用重新启动前该字段的值并不会发生改变| 
| 通过iTunes进行备份 | 不会 |
| 通过iTunes对备份进行还原 | 会 |