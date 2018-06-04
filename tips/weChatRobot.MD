## weChatRobot

把自己的个人微信号变成一个微信机器人

1. 区分不同的消息类型、来源、发送者，自定义收到特定消息后的回复。
2. 接入图灵机器人的接口，来做个回复机器人，类似以前的小黄鸡。

#### 准备

1. 一台Linux服务器
2. 一点python基础

#### 步骤

1. 在服务器上安装至少Python2.7.*以后版本的，并且使用命令pip install itchat安装itchat。
2. 编写Python脚本，根据自己需求写自定义回复，参考[itchat](https://github.com/littlecodersh/ItChat)文档写脚本。这样已经可以实现依据不同的消息发送者，发送来源，消息类型来自定义回复。
3. 如果还需要接入图灵机器人，去注册一个[图灵账号](http://www.tuling123.com)，然后参考图灵文档，生成一个自己的机器人，每个免费账号可以有5个，每个机器人每天1000次接口调用，把收到的消息转发给图灵机器人，把机器人返回的消息发送出去。
4. 把脚本部署到你自己的服务器上，setpid ***.py（你的脚本），让它一直运行，打完收工。

参考代码我已经放到[这里](https://github.com/supergithuber/supergithuber.github.io/blob/master/code/wechat.py)上，需要的可以参考下，或者直接把我的代码拷到你服务器，修改为自己的图灵账号就可以

#### 参考链接

##### 1. [itchat](https://github.com/littlecodersh/ItChat)
##### 2. [图灵文档](http://www.tuling123.com/help/h_cent_webapi.jhtml)