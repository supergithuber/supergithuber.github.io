## iOS编码规范

官方的编码规范文档 [Naming Basics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingBasics.html)

### 1. 命名规则

#### 1.1 通用命名规则

  通常指变量，常量，属性，参数，函数等的的命名规范[General Principles](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingBasics.html#//apple_ref/doc/uid/20001281-1001751)。
  
  【要】自我描述：用英文描述自身的意义，杜绝拼音，过度缩写或者无意义的命名
  
  【要】驼峰命名规则，有些特殊的不需要驼峰，例如：FTP、WWW
  
  【不要】自我指涉：末尾加上自己类型的后缀；通知、掩码的命名除外
  
命名       |说明          
------- | --------------
person|这是NSObject类型对象，这样可以
personObject|NSObject类型对象，这样不合法
NSUnderlineByWordMask|掩码这样写合法
NSTableViewColumnDidMoveNotification|通知这样写也合法

#### 1.2 缩写规范

  通常不应该缩写单词，除非是一些总所周知的缩写
  
  * 允许使用在C语言时代就存在的缩写，比如alloc和getc
  * 使用计算机行业通用的缩写。包括但是不限于HTML、URL、RTF、HTTP、TIFF、JPG、PNG、GIF、LZW、ROM、RGB、CMYK、MIDI、FTP。

#### 1.3 方法命名规范

* 方法名要准守驼峰原则，除非该方法以通用缩写开头，例如：HTTP，这样该规则可以忽略