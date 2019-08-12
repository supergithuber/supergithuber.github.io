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

输入如下：

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

