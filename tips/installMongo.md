## Mac上安装指定版本Mongodb

1. 通过[官网](https://www.mongodb.com/download-center#community)获取下载地址，类似：https://fastdl.mongodb.org/osx/mongodb-osx-ssl-x86_64-4.0.9.tgz，或者直接下载好tgz格式的压缩包
2. cd /usr/local
3. 如果下载好压缩包，就解压到上述目录下。如果没下载好，就通过curl下载，sudo curl -O https://fastdl.mongodb.org/osx/mongodb-osx-ssl-x86_64-4.0.9.tgz，并解压
4. 将文件夹重命名为mongodb
5. 添加到环境变量中
```
export PATH=/usr/local/mongodb/bin:$PATH
```
6. 创建数据存放路径
```
sudo mkdir -p /usr/local/var/mongodb
```
7. 创建日志文件路径
```
sudo mkdir -p /usr/local/var/log/mongodb
```
8. 给予上述路径读写权限
```
sudo chown [your_name] /usr/local/var/mongodb
sudo chown [your_name] /usr/local/var/log/mongodb
```
9. 运行
    
后台运行
```
mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork
```
如果不想在后端运行，而是在控制台上查看运行过程可以直接设置配置文件启动：
```
mongod --config /usr/local/etc/mongod.conf

```