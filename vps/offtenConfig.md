## CentOS常用配置

### ssh端口号

1. 修改文件**/etc/ssh/sshd_config**下的端口号，新增，不删除原来的22，防止失败登不上去
2. 改完后service sshd restart
3. CentOS7以后的系统，使用firewall，不再使用iptables做防火墙，如果开启了firewall防火墙，要添加允许端口`firewall-cmd --add-port=XXXX/tcp --permanent` xxxx表示你刚刚新加的端口号
4. 如果使用阿里云的，还要在安全组里配置下
5. 最后改完logout确定下成功，然后可以回去把22删除，再重启下ssh `service sshd restart`

### git

```undefined
yum install git
```

### 查看磁盘空间

```shell
df -hl 
```

### crontab

```shell
##安装
yum -y install vixie-cron
yum -y install crontabs
##启动
systemctl start crond.service
##关闭
systemctl stop crond.service
##重启
systemctl restart crond.service
##开机运行
systemctl enable crond.service
```

### nvm

```shell
## 下载nvm
wget https://codeload.github.com/creationix/nvm/zip/master
## 解压
unzip master
## 安装
cd nvm-master
./install.sh
## 添加环境变量
source ~/.bashrc
## 查看版本
nvm --version
```



### 压缩

```shell
yum install zip unzip
```

### mongodb

```shell
yum install mongodb-server mongodb -y
```

### Python

```shell
#一些依赖
sudo yum groupinstall "Development tools"
sudo yum -y install zlib zlib-devel
sudo yum -y install libffi-devel

#安装
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xJf Python-3.7.0.tar.xz
cd Python-3.7.0
sudo ./configure
sudo make
sudo make install

#创建软连接，修改默认python版本
mv /usr/bin/python /usr/bin/python.bak
ln -s /usr/local/bin/python3.7 /usr/bin/python
mv /usr/bin/pip /usr/bin/pip.bak
ln -s /usr/local/bin/pip3.7 /usr/bin/pip

#yum无法使用，要修改下面两个文件的顶部，把#! /usr/bin/python改为#! /usr/bin/python2
vim /usr/libexec/urlgrabber-ext-down
vim /usr/bin/yum
```

