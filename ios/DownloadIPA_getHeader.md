## 下载ipa并获取头文件

#### 1. 下载[class-dump](http://stevenygard.com/projects/class-dump), 下载dmg并把可执行文件复制到/usr/bin这个目录下。
#### 2. 给文件可执行权限：sudo chmod 777 /usr/bin/class-dump，如果是10.11以上系统，需要进入安全模式，关闭Rootless。
#### 3. 去pp助手网页版下载越狱版的对应APP。这里有一个下载ipa的python脚本，可以用下，它使用Xpath解析下载页面的标签，获取下载地址，由于下载地址是使用base64编码的，解码后获取下载地址。

```python
#! /usr/bin/env python3

import requests
import shutil
from lxml.etree import HTML
from base64 import b64decode
from sys import argv

def main():
    apps = argv[1:]
    for app in apps:
        req = requests.get(app)
        sel = HTML(req.content)
        title = sel.xpath('//h2[contains(@class, "app-title")]/text()')[-1]
        encoded = sel.xpath('//a[@class="btn-install-x"]/@appdownurl')[-1]
        decoded = b64decode(encoded).decode('utf8')
        print("%s: %s" % (title, decoded))
        
        resp = requests.get(decoded, stream=True)
        assert(resp.status_code == 200)
        with open('%s.ipa' % title, 'wb') as ipa:
            print('Downloading ipa %s...' % title)
            resp.raw.decode_content=True
            shutil.copyfileobj(resp.raw, ipa)
        print('%s downloaded' % title)

if __name__ == '__main__':
    main()
```



#### 4. 解压越狱的ipa，拿到Payload文件夹下的.app文件，放到某个地方，例如~/Desktop/classDump, 使用class-dump执行下面命令：

   ```
   class-dump -H ~/Desktop/classDump/*.app -o ~/Desktop/classDump/folder
   ```

   你需要的header就会出现在folder文件夹下



