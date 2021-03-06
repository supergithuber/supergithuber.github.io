## 搭建shadowSocks

1. 买一台vps，我买的是[vultr](https://www.vultr.com/?ref=7367428)，安装好centos7系统（当然也可以其他系统）。
2. 在终端或者其他ssh客户端（putty），ssh root@[你服务器的ip]连接你的服务器。
3. 执行：
> wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh 
> 安装shadowsocks。
4. 执行：
> chmod +x shadowsocks-all.sh 
> 改为可执行权限。
5. 执行： 
> ./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
> 日志输出。
6. 

```
Which Shadowsocks server you'd select:
1.Shadowsocks-Python
2.ShadowsocksR
3.Shadowsocks-Go
4.Shadowsocks-libev
Please enter a number (default 1):
```
选择一个，我选的是3，go语言的，其他的没试过，这个是成功的。

7. 设置你的密码和端口，牢记这个

```
Congratulations, Shadowsocks-Go server install completed!
Your Server IP        :  45.32.73.59
Your Server Port      :  8989
Your Password         :  teddysun.com
Your Encryption Method:  aes-256-cfb

Welcome to visit: https://teddysun.com/486.html
Enjoy it!
```
最后会有这样的打印，记下来。

##### 最后在你的客户端下载shadowsocks，mac和windows在github上有；iOS和android可以下载superwingy, shadowrocket类似的VPN客户端；chrome浏览器也有类似插件，输入服务器ip，端口，密码，加密方式就可以

##### 修改配置的配置文件在**/etc/shadowsocks-go/config.json**这个目录下，修改完后要重启**/etc/init.d/shadowsocks-go restart**

-------

### 开启BBR加速

#### 开启TCP Fast Open
```
vim /etc/rc.local

# 在最后一行增加以下内容
echo 3 > /proc/sys/net/ipv4/tcp_fastopen

# 然后
vim /etc/sysctl.conf

# 在最后一行增加：
net.ipv4.tcp_fastopen = 3

# 编辑配置文件
vim /etc/shadowsocks/config.json
# 添加一项
"fast_open":true

# 最后重启
/etc/init.d/shadowsocks restart

```

#### 安装脚本

```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh

chmod +x bbr.sh

./bbr.sh
```

#### 查看内核

```
uname -r
```

是不是新版的

#### 检查是否开启BBR

```
sysctl net.ipv4.tcp_available_congestion_control
# 返回值一般为：net.ipv4.tcp_available_congestion_control = bbr cubic reno

sysctl net.ipv4.tcp_congestion_control
# 返回值一般为：net.ipv4.tcp_congestion_control = bbr

sysctl net.core.default_qdisc
# 返回值一般为：net.core.default_qdisc = fq

lsmod | grep bbr
# 返回值有tcp_bbr则说明已经启动
```

##### 参考链接
1. [轻松在 VPS 搭建 Shadowsocks 翻墙](https://www.diycode.cc/topics/738)
2. [CentOS7增加或修改SSH端口号](https://blog.csdn.net/ausboyue/article/details/53691953)
3. [开启BBR加速](https://rootrl.github.io/2017/10/11/Vultr-Centos%E5%AE%89%E8%A3%85shadowsocks%E6%9C%8D%E5%8A%A1%E7%AB%AF%E5%B9%B6%E5%BC%80%E5%90%AFBBR%E5%8A%A0%E9%80%9F/)
4. [下载shadowsocks客户端](https://github.com/shadowsocks)