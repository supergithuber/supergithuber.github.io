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

