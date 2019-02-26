## Python发送邮件

### 1. 安装支持库

安装smtplib库

```
pip install secure-smtplib
```

安装email库

```
pip install email
```

### 2. 打开邮箱SMTP功能

* 不同邮箱打开SMTP的方式不一样，一般都在邮箱设置里。
* 一般都不会在自己的服务器上搭建smtp服务器，会用一些公司的服务器，可以去网上搜下服务器地址和端口号。

### 3. 接口介绍

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

#### Python创建 SMTP 对象：

```
import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
```

> 参数说明：
> 
> host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
> 
> port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
> 
> local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。

#### Python SMTP 对象使用 sendmail 方法发送邮件：

```
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
```

> 参数说明：
> 
> from_addr: 邮件发送者地址。
> 
> to_addrs: 字符串列表，邮件发送地址。
> 
> msg: 发送消息
> 

这里要注意一下第三个参数，msg 是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。这个格式就是 smtp 协议中定义的格式.

