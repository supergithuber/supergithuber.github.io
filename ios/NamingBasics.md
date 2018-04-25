# iOS编码规范

官方的编码规范文档 [Naming Basics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingBasics.html)

## 1. 命名规则

### 1.1 通用命名规则

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

### 1.2 缩写规范

  通常不应该缩写单词，除非是一些总所周知的缩写
  
  * 允许使用在C语言时代就存在的缩写，比如alloc和getc
  * 使用计算机行业通用的缩写。包括但是不限于HTML、URL、RTF、HTTP、TIFF、JPG、PNG、GIF、LZW、ROM、RGB、CMYK、MIDI、FTP。

### 1.3 方法命名规范

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

### 1.4 Accessor命名规范

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

### 1.5 delegate命名规范

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

### 1.6 Private方法命名规范

大部分情况下，私有方法的命名和公有方法的命名规则是一样的。然而，通常情况下应该给私有方法添加一个前缀，目的是和公有方法区分开。尽管这样，这种给私有方法加前缀的命名方式有可能引起一些奇怪的问题。问题就是：当你从Cocoa framework（即Cocoa系统库）中的某个类派生出来一个子类时，你并不知道你的子类中定义的私有方法是否覆盖了父类的私有方法，即有可能你自己在子类中实现的私有方法和父类中的某个私有方法同名。在运行时，这极有可能导致一些莫名其妙的问题，并且调试追踪问题的难度也是相当大。

Cocoa frameworks（Cocoa系统库）中的私有方法通常以一个下划线“ _ ”开头，用于标记这些方法是私有的(比如， _fooData ) ,这大概就是Apple工程师的开发习惯。基于这个事实，提供以下两条建议

#### 1. 禁止使用下划线“ _ “作为私有方法的开头。Apple已经预留这种私有方法的命名习惯
#### 2. 如果你是要子类化Cocoa Frameworks中的一个非常庞大复杂的类（比如NSView或UIView），并且你想绝对的确保你自己的子类中的私有方法名和父类中的私有方法名不重复。你可以添加一个你自己的前缀作为私有方法的前缀，这个前缀应该尽可能的独特。也许这个前缀是基于你公司或者项目的缩写，比如”XX_“。尽管给私有方法增加前缀看起来和”方法存在于他们的类的命名空间中“这一之前的说法有些冲突，但此处的意图是：为子类私有方法添加前缀仅仅是为了保证子类方法和父类方法名称不冲突。

### 1.7 Catogory命名规范

#### 1. category中不要声明属性和成员变量，尽管可以使用runtime方法来实现，但是这样会导致不方便管理
#### 2. 避免category中的方法覆盖系统方法。可以使用前缀来区分系统方法和category方法。但前缀不要仅仅使用下划线”_“
#### 3. 如果一个类比较复杂，建议使用category的方式组织代码

### 1.8 Class命名规范

class的名称应该由两部分组成，前缀+名称。即，class的名称应该包含一个前缀和一个名词

### 1.9 Protocol命名规范

如果proctocol不仅声明了一堆相关方法，还关联了某个class。这种关联class的protocol的命名取决于关联的class，然后再后面再加上protocol或delegate用于显示的声明这是一份协议

命名  | 说明
---- | -----
UITableViewDelegate    |   OK
NSObjectProtocol      |    OK

### 1.10 Notification命名规范

#### 1. 规则：[Name of associated class] + [Did | Will] + [UniquePartOfName] + Notification

```
NSApplicationDidBecomeActiveNotification
NSWindowDidMiniaturizeNotification
NSTextViewDidChangeSelectionNotification
NSColorPanelColorDidChangeNotification
```

#### 2. object通常是指发出notification的对象，如果在发送notification的同时要传递一些额外的信息，请使用userInfo，而不是object

#### 3. 如果某个通知是为了告知外界某个事件"即将"发生或者"已经"发生，则请在通知名称中使用“will”或者“did”这样的助动词，见上

### 1.11 Constant命名规范

可以使用k开头为constant命名，[Constants规范](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingIvarsAndTypes.html)

不要使用预处理指令创建常量

