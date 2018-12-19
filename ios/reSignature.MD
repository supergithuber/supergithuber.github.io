## Resignature

无越狱设备，需要下载已经脱壳的越狱应用








#### 帮助命令

1. 查看ipa签名信息（Playload文件夹下的那个）: codesign -vv -d WeChat.app 
2. 查看本机所有证书(重签名要用到): security find-identity -v -p codesigning
3. 查看可执行文件的加密信息（Playload文件夹下的那个里头的可执行文件）: otool -l WeChat | grep crypt 

