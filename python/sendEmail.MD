## Python发送邮件

[项目地址](https://github.com/supergithuber/sendEmail)

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

### 4. 发送纯文本邮件

我使用的是谷歌邮箱发送，使用的也是谷歌的smtp服务器

还遇到

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
def gmailSmtp():
    #smtp邮箱服务器地址
    smtp_host = 'smtp.gmail.com'  
    #密码(部分邮箱为授权码) 
    mail_pass = 'your secret' 

    sender = 'wuyishanwuxi@gmail.com'
    receivers = ['361125982@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("Hello", 'utf-8')   # 发送者
    message['To'] =  Header("测试", 'utf-8')        # 接收者
 
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
 
 
    try:
        smtpObj = smtplib.SMTP(smtp_host, 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件", e)

if __name__ == "__main__":
    gmailSmtp()

```

谷歌邮箱要求必须使用安全的tls，所以要走587端口。期间还遇到禁止不安全应用登陆的问题，根据打印的错误信息去谷歌邮箱的安全设置里头打开”允许不安全的应用登陆“，之后才可以

如果是一般没有那么严格的邮箱系统，就走SMTP的25端口，对应的登陆SMTP服务器的代码段改成：

```python
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(smtp_host, 25)
    #登录到服务器
    smtpObj.login(sender, mail_pass)
```

如果是一些要求SSL登陆的邮箱，例如QQ邮箱，登陆SMTP服务器的代码段就要改成：

```python
smtpObj = smtplib.SMTP_SSL(smtp_host)
```

### 5. 发送带有附件的邮件

### 6. 发送HTML格式的邮件

### 7. 在HTML文本中添加图片

这些可以实现，我没有写代码，可以参考[Python SMTP](http://www.runoob.com/python/python-email.html)