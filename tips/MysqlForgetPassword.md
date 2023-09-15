## Mysql忘记root账号密码

1. 关闭mysql服务
   
   `sudo /usr/local/bin/mysql.server stop`
   
   如果是在mac上，可以直接在设置中点击关闭

2. 进入目录，获取权限，启动安全模式
   
   `cd /usr/local/mysql/bin`
   
   `sudo su`
   
   `./mysqld_safe --skip-grant-tables &`

3. 再打开一个终端，进入mysql
   
   `mysql`
   
   `use mysql`
   
   `flush privileges;`
   
   `ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456';`
   
   `flush privileges;`
   
   `exit;`
   
   有的客户端可能不支持`caching_sha2_password`加密方式，看情况可以改成`mysql_native_password`

4. 最后杀进程
   
   `ps -ef | grep mysql`查看相关的进程，杀死并重启mysql
