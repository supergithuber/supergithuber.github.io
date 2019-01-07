## WeatherMessage

这是一个利用一些免费接口做的工具，它每天定时发送天气预报的短信到你手机上，项目的地址在[WeatherMessage](https://github.com/supergithuber/WeatherMessage)。

1. 获取天气信息，[心知天气](https://www.seniverse.com/)，天气的有收费接口，也有免费接口，这里用免费接口就够了。
2. 免费发送短信，[twilio](https://www.twilio.com/)，短信的可以免费给注册的手机发送。

去这两个平台注册账号，看看它们的文档。

当然还有一台linux服务器，这里用的是centos7，安装好Python。

----

##### 1. 代码的地址在[这里](https://github.com/supergithuber/WeatherMessage/blob/master/weather.py)

主要的方法就是：

* 去心知天气获取天气信息。
* 用twilio去给手机发送信息。
* 把每天的信息写入到txt里，并推送到git上。

##### 2. 定时执行脚本

Linux自带crond，没有就安装一下。

编辑crond定时任务

> crond -e

编辑定时任务，格式可以看它的[文档](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)

然后启动重启crond

> service crond restart
 
注意设置下服务器时间

##### 3. 推送到git

之前使用gitPython结合crond，一直有git目录不对的问题。
crond使用的时候是默认系统目录的，我配置了绝对路径还是不行。
后面改用subprocess这个Python库。