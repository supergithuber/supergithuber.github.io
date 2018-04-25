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
* 类、协议、函数、常量、枚举等全局可见内容需要添加三个字符作为前缀。苹果保留对任意两个字符作为前缀的使用权。所以尽量不要使用两个字符作为前缀。禁止使用的前缀包括但不限于：NS,UI,CG,CF,CA,WK,MK,CI,NC
* 禁止在方法前面加下划线“ _ ”。官方SDK经常在私有方法前面加下划线"_"。为了不可预知的意外，禁止在方法前面加下划线
* 方法的命名也应该具有自我描述性。杜绝中文拼音、过度缩写、或者无意义的命名方式
* 如果一个方法代表某个名词执行的动作，则该方法应该以一个动词开头，如下

```
- (void)invokeWithTarget:(id)target;
- (void)selectTabViewItem:(NSTabViewItem *)tabViewItem
```

* 如果方法返回接收者的某个属性，那么请直接以属性名作为方法名
* 所有参数前面都应该添加关键字，参数之前的单词尽量能描述参数的意义

#### 1.4 Accessor命名规范

属性的set和get方法 [General Rules](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingMethods.html)

名词

```
- (NSString *)title;
- (void)setTitle:(NSString *)aTitle;
```

形容词

```
- (BOOL)isEditable;
- (void)setEditable:(BOOL)flag;
```

动词

```
- (BOOL)showsAlpha;
- (void)setShowsAlpha:(BOOL)flag;
```

#### 1.5 delegate命名规范

* 以触发消息的对象名开头，省略类名前缀并且首字母小写

```
- (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row;
- (BOOL)application:(NSApplication *)sender openFile:(NSString *)filename;
```

* 除非delegate方法只有一个参数，即触发delegate方法调用的delegating对象，否则冒号是紧跟在类名后面的

```
- (BOOL)applicationOpenUntitledFile:(NSApplication *)sender;
```

* 发送通知后再触发delegate方法是一个例外：当delegate方法的调用是为了告诉delegate对象，某个通知已经被发送时，这个delegate方法的参数应该是通知对象，而非触发delegate方法的对象

```
- (void)windowDidChangeScreen:(NSNotification *)notification;
```

* 使用did或will这两个情态动词通知delegate对象某件事已经发生或将要发生

```
- (void)browserDidScroll:(NSBrowser *)sender;
- (NSUndoManager *)windowWillReturnUndoManager:(NSWindow *)window;
```

#### 1.6 Private方法命名规范

