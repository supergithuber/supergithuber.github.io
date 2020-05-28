## 数据库操作

- mysql数据库备份

```shell
mysqldump -h127.0.0.1 -uroot -p123456 atoslNew>atoslNew.sql
```

- mysql数据库恢复

```shell
mysql -h127.0.0.1 -uroot -p123456 atoslNew<./atoslNew.sql
```

- mysql数据库查表大小

```shell
USE information_schema;

SELECT TABLE_SCHEMA, SUM(DATA_LENGTH)/1024/1024 FROM TABLES GROUP BY TABLE_SCHEMA;
```



- mongodb备份

```shell
mongodump -h dbhost -d dbname -o dbdirectory
```

- mongodb恢复

```shell
mongorestore -h <hostname><:port> -d dbname <path>   //default port: 27017
```

- 查看数据库大小

```shell
db.stats();
db.stats(1024);//以kb为单位返回
```

```json
//返回示例
{
    "db" : "xxx",   //当前数据库
    "collections" : 27,  //当前数据库多少表 
    "objects" : 18738550,  //当前数据库所有表多少条数据
    "avgObjSize" : 1153.54876188392, //每条数据的平均大小
    "dataSize" : 21615831152.0,  //所有数据的总大小
    "storageSize" : 23223312272.0,  //所有数据占的磁盘大小 
    "numExtents" : 121,
    "indexes" : 26,   //索引数 
    "indexSize" : 821082976,  //索引大小 
    "fileSize" : 25691160576.0,  //预分配给数据库的文件大小
    "nsSizeMB" : 16,
    "dataFileVersion" : {
        "major" : 4,
        "minor" : 5
    },
    "extentFreeList" : {
        "num" : 1,
        "totalSize" : 65536
    },
    "ok" : 1.0
}
```

