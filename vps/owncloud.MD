## owncloud

##### 1. 安装httpd, php, mariadb
yum install httpd -y

yum install php -y

yum install mariadb mariadb-server -y

##### 2. 重启apache服务

systemctl restart httpd

遇到的问题，启动apache服务失败：

> Job for httpd.service failed because the control process exited with error code. See "systemctl status httpd.service" and "journalctl -xe" for details.

通过提示命令看看日志，发现80端口已经被占用

> (98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:80

看看是谁占用了80端口， 然后杀了它：

> netstat -tulpn | grep :80

这里就输入占用80端口的哪个pid

> kill -9 [PID]

重启一下apache并且看看状态：

systemctl restart httpd

systemctl status httpd

##### 3.启动mariadb

> systemctl start mariadb

##### 4.初始化数据库服务

> mysql_secure_installation

遇到问题：

> ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

首次本来是不需要输入密码的，但是可能是初始化的时候，mariadb给了一个默认密码，又找不到，就当做忘记密码来处理，重置密码

##### 4.1 停掉服务

> systemctl stop mariadb

##### 4.2 使用跳过授权的方式启动 mariadb

> mysqld_safe --skip-grant-tables &

这样会打印出进程号，类似这样，这里进程号是14411

> [1] 1441

> [root@centos7 ~]# 170531 02:10:28 mysqld_safe Logging to '/var/log/mariadb/mariadb.log'.

> 170531 02:10:28 mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql 

可以看下

> ps -ef | grep 14411

##### 4.3 当跳过授权启动时，可以不需要密码直接登陆数据库。登陆更新密码即可

进入数据库，更新密码

> mysql

>  \>use mysql; 
> 
>  \>UPDATE user SET password=password('newpassword') WHERE user='root';
> 
>  \>flush privileges; 
> 
>  \>exit;
> 

##### 4.4 关闭跳过授权启动的进程

> kill -9 14411

##### 4.5 启动mariadb

> systemctl start mariadb

然后继续初始化数据库

>[root@miami etc]# mysql_secure_installation
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
  SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

> In order to log into MariaDB to secure it, we'll need the current
 password for the root user.  If you've just installed MariaDB, and
 you haven't set the root password yet, the password will be blank,
 so you should just press enter here.
 Enter current password for root (enter for none): #回车
  OK, successfully used password, moving on...

>  Setting the root password ensures that nobody can log into the MariaDB
>  root user without the proper authorisation.

>  Set root password? [Y/n] y  #   选择Y设置密码

>  New password:
  Re-enter new password:
  Reloading privilege tables..
   ... Success!


> By default, a MariaDB installation has an anonymous user, allowing anyone
 to log into MariaDB without having to have a user account created for
 them.  This is intended only for testing, and to make the installation
 go a bit smoother.  You should remove them before moving into a
 production environment.

> Remove anonymous users? [Y/n] #选择Y删除匿名账户
... Success!

> Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

> Disallow root login remotely? [Y/n] y #选择Y禁止root用户从远程登录
... Success!

> By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

> Remove test database and access to it? [Y/n] y #选择Y删除test数据库并取消对其的访问权限
    - Dropping test database...
    ... Success!
- Removing privileges on test database...
... Success!

> Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

> Reload privilege tables now? [Y/n] y #选择Y刷新授权表，让初始化的设定立即生效
... Success!

> Cleaning up...

> All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

> Thanks for using MariaDB!