## 删除最近文件

```shell
#!/bin/bash
desRootPath="/Users/longpufu/jenkins/workspace/BigoUITestBuildRunner/"

ls -l
##删除目标目录下超过2天以前的dsyms
find ${desRootPath} -mtime +1 -type d -name "*.zip" | xargs rm -rf
##目标目录当前拥有的文件
echo "目标目录当前还有的文件"
ls -la ${desRootPath}

echo "完成！"
```

