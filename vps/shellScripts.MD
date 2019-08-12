## shell脚本实例

#### 1. 文件以日期命名，并写入磁盘使用情况

```
#!/bin/bash 
#################################################
#文件以日期命名，并写入磁盘使用情况
#################################################
d=`date +%Y-%m-%d` ##获取日期
logfile=$d.log ##定义日志文件名
df -h > $logfile ##向文件写入磁盘使用情况
```

输出如下：

```
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   233Gi  205Gi   25Gi    90% 2889935 9223372036851885872    0%   /
devfs          194Ki  194Ki    0Bi   100%     670                   0  100%   /dev
/dev/disk1s4   233Gi  2.0Gi   25Gi     8%       2 9223372036854775805    0%   /private/var/vm
/dev/disk3s1   466Gi   16Gi  449Gi     4%  147433 9223372036854628374    0%   /Volumes/Solid
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
```

#### 2. 统计日志文件中各个IP的访问量

```
#!/bin/bash
#################################################
##取文件IP|排序|去重并统计各个IP重复数量|排序
#################################################
awk '{print $1}' ip.txt |sort -n |uniq -c |sort -n
```

例如有一个这样的文件: ip.txt

```
123 -sdfjukhesdjkfghjkldf 
456 -jsdigkhndjfgjd 
789 -dsfjkdhfjkhsdjkfhsjk 
123 -sdfhfjkhsjklaj 
789 -jfgduhdjkfghjkdf 
123 -dhsfgjkhsdjkghjkdf
```

通过刚刚的脚本，输出如下

```
1 456
2 789
3 123
```

#### 3. 计算Linux系统所有进程占用内存之和

```
#!/bin/bash
#################################################
#计算Linux系统所有进程占用内存之和
#################################################
sum=0
#利用for循环调取每一项进程所使用的内存，并依次求和
for mem in `ps aux |awk '{print $6}' |grep -v 'RSS'`
do
 sum=$[$sum+$mem] ##内存求和
done
echo "the usered mem $sum" ##输出结果
```

输出如下：

```
the usered mem 32374
```

#### 4. 监控远程机器的存活，发现宕机示警

```
#!/bin/bash
#################################################
#监控远程机器的存活，发现宕机示警
#################################################
#假设远程机器IP为114.114.114.114
ip=114.114.114.114
d=`date +%Y-%m-%d` ##获取日期
#while循环做循环监控，"while ："为死循环
while :
do
#使用ping命令，取丢包率的数值作为存活的判断依据
n=`ping -c2 $ip 2> /dev/null |grep 'received' |awk -F 'received, |%' '{print $2}'`
n1=`echo $n |sed 's/[0-9]//g'`
#判断取值是否为空
 if [ -z "$n" ]
 then
 echo "error"
 exit
#判断取值是否为数字
 elif [ -n "$n1" ]
 then
 echo "error"
 exit
#若丢包率不低于20%，则发送告警
 elif [ $n -ge 20 ]
 then
 #这里也可做外发邮件告警
 echo "more loss"
 else
 echo "$d : $ip is OK" > ip_monitor.log
 fi
#监控间隔为30秒
sleep 30
done
```

#### 5. 批量修改指定目录下文件名、打包并还原文件名

```
#!/bin/bash
#################################################
#批量修改指定目录下文件名、打包并还原文件名
#################################################
#将目标文件夹下的所有指定类型文件的文件名查找存在指定文件中
find /home/scripts -type f -name "*.txt" > /home/scripts/txt.list
#通过for循环遍历所有文件，并依次改名
for f in `cat /home/scripts/txt.list`
do
 mv $f $f.bak
done
#定义一个时间命名的目录作为打包文件的目录
d=`date +%F`
mkdir /home/scripts/txt_$d
#将所有改名文件依次拷贝到打包文件的目录下
for f in `cat /home/scripts/txt.list`
do
 cp $f.bak /home/scripts/txt_$d
done
#进入指定目录下进行打包
cd /home/scripts
tar -czvf txt.tar.gz txt_$d
#还原文件名
for f in `cat /home/scripts/txt.list`
do
 mv $f.bak $f
done
```

#### 6. 判断本机80端口是否监听，如果不存在，则重启服务并发送邮件告警

```
#!/bin/bash
###########################################################
#判断本机80端口是否监听，如果不存在，则重启服务并发送邮件告警
###########################################################
#判断本机80端口是否监听，并执行相应动作（使用命令行作为判断条件时，命令行正确执行即满足if条件，且用于判定的命令行不需要加反引号）
if netstat -ntpl |grep -q ':80 '
 then
 exit
 else
 #这里也可做外发邮件告警
 echo "error"
 #service nginx restart
fi
#判断是否启动成功，如未成功，则将错误信息通过邮件进行告警
n=`pgrep -l httpd |wc -l` #列出所有httpd进程的pid
if [ $n -eq 0 ]
 then
 touch /tmp/nginx_start.err
 /usr/local/nginx/sbin/nginx start 2> /tmp/nginx_start.err
fi
if [ -s apache_start.err ] #if -s 选项，文件大小非0时为真
 then
 #这里也可做外发邮件告警
 echo "error"
fi
```

#### 7. 多地备份数据库（本地保留一周、远程保留一月）

```
#!/bin/bash
###########################################################
#多地备份数据库（本地保留一周、远程保留一月）
#date +%Y # 年份(四位) eg: 2018
#date +%y # 年份后两位 eg: 18
#date +%m # 月 eg: 07
#date +%d # 日 eg: 10
#date +%H # 24小时 eg: 11
#date +%M # 分 eg: 37
#date +%S # 秒 eg: 24
#date +%w # 星期(0-6) 0 表示周日
#date +%F # 完整日期 =%Y-%m-%d 
#date +%T # =%H:%M:%S 时间 eg: 10:46:45
###########################################################
d1=date +%w
d2=date +%y-%m-d
bakdir='/backup'
r_bakdir='远程备份的IP地址':'远程备份的目录' #通过ssh同步
rs_bakdir='远程备份的IP地址'::'模块名称' #通过服务同步
#定义接下来的命令涉及到的所有的正确输出记录在正确日志的目录下，所有的错误输出记录在错误日志的目录下
exec 1> '正确日志的目录' 2>'错误日志的目录'
echo "mysql backup begin at `date +"%F %T"`"
#备份到本地机器的文件以星期命名，周期为7天，超出7天后，同名的旧文件会被新文件覆盖
mysqldump -u'指定的用户' -p'指定的密码' '指定的数据库' > $bakdir/$d1.sql
#备份到远程机器的文件以日期命名，周期为31天，超出31天后，同名的旧文件会被新文件覆盖
rsync -az $bakdir/$d1.sql $r_bakdir/$d2.sql
echo "mysql backup end at `date +"%F %T"`"
```