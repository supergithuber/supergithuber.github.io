## mac打开对NTFS的支持

#### 1. 把磁盘插入电脑

> diskutil list

查看磁盘的名字

```
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *2.0 TB     disk2
   1:                        EFI EFI                     209.7 MB   disk2s1
   2:                  Apple_HFS HFS+                    1.5 TB     disk2s2
   3:       Microsoft Basic Data NTFS                    255.9 GB   disk2s3
   4:       Microsoft Basic Data FAT32                   255.7 GB   disk2s4
```

例如我这边的名字就叫HFS+，NTFS，FAT32那一列

#### 2. 修改 /etc/fstab文件

打开文件

> sudo vi /etc/fstab
 
写入

> LABEL=NAME none ntfs rw,auto,nobrowse

其中的NAME就是你磁盘对应的name

如果有名字有空格要转义\040

rw代表可读可写

nobrowse代表finder里不显示这个分区，必须这么做才可以

#### 3. 打开快捷方式

既然不显示分区，就要做个快捷方式

> sudo ln -s /Volumes/HTFS ~/Desktop/HTFS_link
 
#### 4. 隐藏快捷方式

把快捷方式拖入Finder中的侧边栏

然后把刚刚在桌面上的隐藏了

> mv HTFS_link .HTFS_link
 

----
另外有一些软件也可以使用：

1. paragon NTFS（收费）
2. mounty ntfs（原生的封装）
3. Tuxera NTFS(收费)
4. [fuse for macos](https://osxfuse.github.io/)