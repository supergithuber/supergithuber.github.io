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



### 相关连接

[项目地址](http://dumpsterventures.com/jason/httpry/)