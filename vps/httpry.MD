## httpry 工具

* 一个使用C语言开发的封包嗅探器，用来记录和显示http流量。
* 它可以作为一个后台进程记录实时流量并输出到文件，由于具有轻型和灵活的特性，所以它可以很容易适应不同的应用程序。

### 使用场景

> 查看你服务器上访问过的页面
> 
> 统计并分析所有访问记录
> 

### 安装（centOS下）

##### 1. 安装依赖包，在ubuntu下应该就是apt-get

```
yum install wget gcc make libpcap libpcap-devel
```

##### 2. 创建相关数据目录

```
mkdir -p /usr/local/man/man1
mkdir -p /usr/man/man1/
```

##### 3. 编译httpry

```
wget http://dumpsterventures.com/jason/httpry/httpry-0.1.8.tar.gz
tar zvxf httpry-0.1.8.tar.gz
cd httpry-0.1.8
make
make install
mkdir /usr/local/share/httpry-0.1.8
mv doc scripts $_

```

##### 4. 用法

```
$ httpry -h

httpry version 0.1.8 -- HTTP logging and information retrieval tool
Copyright (c) 2005-2014 Jason Bittel <jason.bittel@gmail.com>
Usage: httpry [ -dFhpqs ] [-b file ] [ -f format ] [ -i device ] [ -l threshold ]
              [ -m methods ] [ -n count ] [ -o file ] [ -P file ] [ -r file ]
              [ -t seconds] [ -u user ] [ 'expression' ]

   -b file      write HTTP packets to a binary dump file
   -d           run as daemon
   -f format    specify output format string
   -F           force output flush
   -h           print this help information
   -i device    listen on this interface
   -l threshold specify a rps threshold for rate statistics
   -m methods   specify request methods to parse
   -n count     set number of HTTP packets to parse
   -o file      write output to a file
   -p           disable promiscuous mode
   -P file      use custom PID filename when running in daemon mode 
   -q           suppress non-critical output
   -r file      read packets from input file
   -s           run in HTTP requests per second mode
   -t seconds   specify the display interval for rate statistics
   -u user      set process owner
   expression   specify a bpf-style capture filter

Additional information can be found at:
   http://dumpsterventures.com/jason/httpry
```

### 使用范例

##### 1. 监听特定网卡

```
httpry -i eth0
```

##### 2. 以二进制形势存储结果，并使用httpry打开

```
httpry -i eth0 -b output.dump  //存储

httpry -r output.dump  //打开
```

##### 3. 将httpry数据以可读文件保存

```
httpry -i eth0 -o /tmp/output.txt
```

##### 4. 监视指定的HTTP方法

```
httpry -i eth0 -m get,head
```

##### 5. 分析记录

编译安装时候，有一个perl脚本用来帮助我们分析httpry输出。该脚本在/usr/local/share/httpry-0.1.8/scripts/目录下

> hostname : 显示一些列唯一主机名
> 
> find_proxies：检测web代理
> 
> search_terms：查找并计算在搜索服务中输入搜索词
> 
> content_analysis：查找包含特定关键字的URI
> 
> xml_output：以xml格式输出
> 
> log_summary：生成日志摘要
> 
> db_dump：将日志转存到mysql数据库中

要先用第三点提到的 -o 生成可读文件/tmp/output.txt，然后再对文件执行脚本进行分析

```
cd /usr/local/share/httpry-0.1.8/scripts/
perl ./parse_log.pl -p plugins/log_summary.pm  /tmp/output.txt
```

parse_log.pl执行完后，会在/usr/local/share/httpry-0.1.8/scripts/目录下生成分析结果文件log_summary.txt。类似下面

```
$ cat log_summary.txt 

LOG SUMMARY

Generated:      Wed May 25 13:57:40 2016
Total lines:    14
Total run time: 0.0 secs


REQUESTS BY HOUR

  0%   0%   0%   0%   0%   0%   0%   0%   0%   0%   0%   0% 
  |----|----|----|----|----|----|----|----|----|----|----|
 00   01   02   03   04   05   06   07   08   09   10   11  

  0% 100%   0%   0%   0%   0%   0%   0%   0%   0%   0%   0% 
  |----|----|----|----|----|----|----|----|----|----|----|
 12   13   14   15   16   17   18   19   20   21   22   23  


15/5 VISITED HOSTS

2	28.6%	hi-linux.com
2	28.6%	www.hi-linux.com
1	14.3%	www.163.com
1	14.3%	www.qq.com
1	14.3%	www.baidu.com


15/1 TOP TALKERS

7	100.0%	192.168.119.100


15/1 RESPONSE CODES

7	100.0%	200
```

产生所有报表

```
perl ./parse_log.pl -d plugins /tmp/output.txt
ls -l *.txt
```

parse_log.pl执行完后，会在httpry-0.1.8/scripts目录下生成一些分析结果文件(*.txt/xml)

### 相关连接

[项目地址](http://dumpsterventures.com/jason/httpry/)

[github](https://github.com/jbittel/httpry)