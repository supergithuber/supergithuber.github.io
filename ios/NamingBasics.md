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

### 1.12 Exception命名规范

类似于Notification命名规范
[Prefix] + [UniquePartOfName] + Exception

```
NSColorListIOException
NSColorListNotEditableException
NSDraggingException
NSFontUnavailableException
NSIllegalSelectorException
```

## 2. 编码规则

### 2.1 Initialize规范

[**Tips and Techniques for Framework Developers**](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/FrameworkImpl.html)

* (void)initialize类方法先于其他的方法调用。且initialize方法给我们提供了一个让代码once、lazy执行的地方。initialize通常被用于设置class的版本号.[Versioning and Compatibility](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/FrameworkImpl.html#//apple_ref/doc/uid/20001286-1001777)

initialize方法的调用遵循继承规则(所谓继承规则，简单来讲是指：子类方法中可以调用到父类的同名方法，即使没有显式调用[super xxx])。如果我们没有实现initialize方法，运行时初次调用这个类的时候，系统会沿着继承链，先后给继承链上游中的每个超类发送一条initialize消息，直到某个超类实现了initlialize方法，才会停止向上调用。因此，在运行时，某个类的initialize方法可能会被调用多次(比如：一个子类没有实现initialize方法)。
比如：有三个类：SuperClass、SubClass和FinalClass。他们的继承关系是这样的FinalClass->SubClass->SuperClass，只实现了SuperClass方法的initialize方法。

```
// SuperClass
@implementationSuperClass
+ (void)initialize {
    NSLog(@"superClass initalize");
}
@end
// 初始化FinalClass
- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    FinalClass *finalC = [FinalClass new];
}
// 控制台输出结果
2018-01-2722:11:03.130365+0800 Demo[67162:11721965] superClass initalize
2018-01-2722:11:03.130722+0800 Demo[67162:11721965] superClass initalize
2018-01-2722:11:03.130815+0800 Demo[67162:11721965] superClass initalize
```

***解释***：

因为FinalClass继承自SubClass，SubClass继承自SuperClass。因为继承体系中只有SuperClass实现了initialize方法，导致初始化FinalClass这个子类时，FinalClass会调用他的父类(SubClass)中的initialize方法。又因为他(FinalClass)的父类(SubClass)也没有实现initialize方法，又会继续沿着继承体系，向上游寻找，最后找到SubClass的父类(SuperClass)。因为SuperClass实现了这个initialize方法，所以调用结束。至于为什么是连续调用了三次SuperClass的initialize方法。因为子类FinalClass的初始化触发了超类SubClass、SuperClass的初始化。所以初始化FinalClass时，实际上使这三个类都得到了初始化的机会，自然就会连续调用三次SuperClass的initialize方法

还是上面那三个类，如果我们又给SubClass实现了initialize方法，那么控制台将会输出如下结果：

```
2018-01-27 22:34:54.697952+0800Load[67652:11780578]superClassinitalize
2018-01-27 22:34:54.698118+0800Load[67652:11780578]subClassinitialize
2018-01-27 22:34:54.698472+0800Load[67652:11780578]subClassinitialize
```

* 【必须】如果我们想要让initialize方法仅仅被调用一次，那么需要借助于GCD的dispatch_once()。如下：

```
+ (void)initialize {
    staticdispatch_once_t onceToken = 0;
    dispatch_once(&onceToken, ^{
        // the initializing code
    }
}
```

【建议】如果我们想在继承体系的某个指定的类的initialize方法中执行一些初始化代码，可以使用类型检查和而非dispatch_once()。如下

```
if (self == [NSFooclass]) {
    // the initializing code
}
```

说了这么多，总而言之，由于任何子类都会调用父类的initialize方法，所以可能会导致某个父类的initialize方法会被调用多次，为了避免这种情况，我们可以使用

1. 类型判断
2. dispatch_once()

这两种方式，以保证initialize中的代码不会被无故调用。

### 2.2 初始化方法规范

Objective-C有designated Initializers和secondary Initializers的概念。

* designated Initializers叫做指定初始化方法。《Effective Objective-C 2.0 编写高质量iOS 与 OS X代码的52个有效方法》中将designated Initializers翻译为”全能初始化方法“。
* designated Initializers方法是指类中为对象提供必要信息以便其能完成工作的初始化方法。

一个类可以有一个或者多个designated Initializers。但是要保证所有的其他secondary initializers都要调用designated Initializers。即：只有designated Initializers才会存储对象的信息。这样的好处是：当这个类底层的某些数据存储机制发生变化时(可能是一些property的变更)，只需要修改这个designated Initializers内部的代码即可。无需改动其他secondary Initializers初始化方法的代码。

#### 1. 所有secondary 初始化方法都应该调用designated 初始化方法
#### 2. 所有子类的designated初始化方法都要调用父类的designated初始化方法。使这种调用关系沿着类的继承体系形成一条链
#### 3. 如果子类的designated初始化方法与超类的designated初始化方法不同，则子类应该覆写超类的designated初始化方法。（因为开发者很有可能直接调用超类的某个designated方法来初始化一个子类对象，这样也是合情合理的，但使用超类的方法初始化子类，可能会导致子类在初始化时缺失一些必要信息）
#### 4. 如果超类的某个初始化方法不适用于子类，则子类应该覆写这个超类的方法，并在其中抛出异常
#### 5. 禁止子类的designated初始化方法调用父类的secondary初始化方法。否则容易陷入方法调用死循环。如下

```
// 超类
@interfaceParentObject : NSObject
@end
@implementationParentObject
    //designated initializer    
    - (instancetype)initWithURL:(NSString*)url title:(NSString*)title {
        if (self = [super init]) {
            _url = [url copy];
            _title = [title copy];
        }
        returnself;
    }
    //secondary initializer
    - (instancetype)initWithURL:(NSString*)url {
        return [self initWithURL:url title:nil];
    }
    @end
// 子类
@interfaceChildObject : ParentObject
@end
    @implementationChildObject
    //designated initializer
    - (instancetype)initWithURL:(NSString*)url title:(NSString*)title {
        //在designated intializer中调用 secondary initializer，错误的
        if (self = [super initWithURL:url]) {
        }
        returnself;
    }
@end
@implementationViewController
    - (void)viewDidLoad {
        [super viewDidLoad];
        // 这里会死循环
        ChildObject* child = [[ChildObject alloc] initWithURL:@"url" title:@"title"];
    }
@end
```

#### 6. 另外禁止在init方法中使用self.xxx的方式访问属性。如果存在继承的情况下，很有可能导致崩溃。[为什么不能在init和dealloc函数中使用accessor方法](https://www.jianshu.com/p/3cf3f5007243)。

### 2.3 初始化错误

1. 调用父类的designated初始化方法初始化本类的对象
2. 校验父类designated初始化方法返回的对象是否为nil
3. 如果初始化当前对象的时候发生了错误，应该给予对应的处理：释放对象，并返回nil。

以下实例列举类初始化阶段可能会存在的错误：

```
- (id)init {
    self = [super init];  // Call a designated initializer here.
    if (self != nil) {
        // Initialize object  ...
        if (someError) {
            [self release];
            self = nil;
        }
    }
    returnself;
}
```

### 2.4 dealloc规范

1. 不要忘记在dealloc方法中移除通知和KVO
2. dealloc 方法应该放在实现文件的**最上面**，并且刚好在 @synthesize 和 @dynamic 语句的后面。在任何类中，init 都应该直接放在 dealloc 方法的下面
3. 在dealloc方法中，禁止将self作为参数传递出去，如果self被retain住，到下个runloop周期再释放，则会造成多次释放crash

```
-(void)dealloc{
    [self unsafeMethod:self];
    // 因为当前已经在self这个指针所指向的对象的销毁阶段，销毁self所指向的对象已经在所难免。
    // 如果在unsafeMethod:中把self放到了autorelease poll中，那么self会被retain住，计划下个runloop周期在进行销毁。
    // 但是dealloc运行结束后，self所指向的对象的内存空间就直接被回收了，但是self这个指针还没有销毁(即没有被置为nil)，导致self变成了一个名副其实的野指针。
    // 到了下一个runloop周期，因为self所指向的对象已经被销毁，会因为非法访问而造成crash问题。
}
```

4. 和init方法一样，禁止在dealloc方法中使用self.xxx的方式访问属性。如果存在继承的情况下，很有可能导致崩溃。