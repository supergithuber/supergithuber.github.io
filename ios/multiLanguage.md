## iOS多语言实现
---
参与过美颜相机的App，Lighten For iOS和insta360Nano的项目，这些项目都实现了多语言适配，现在适配多语言的APP越来越多了，总结一下如何适配多语言。

1. [APP名称的本地化](#first)
2. [代码中字符串的本地化](#second)
3. [多人开发中，私人本地化字符串表](#third)
4. [图片本地化](#fourth)
5. [本地化初始加载的一些知识](#fifth)

### 准备工作
无论是配置什么本地化，都需要做这个准备工作，首先配置需要国际化的语言，在project->Info->Localizations中添加需要添加的语言，如图所示
![multiLanguage_1](https://supergithuber.github.io/img2/multiLanguage_1.png)

我这里添加了两种语言，英文是默认的，我添加了中文简体和法语。
### 1. <span id="first">APP名称的本地化</span>

名称的本地化意思就是，例如“美颜相机”这个APP，在中文系统的iPhone上显示是“美颜相机”，在英文系统的iPhone上显示就是“Beauty Plus”，这里的显示指的是应用图标下的名称。
首先新建一个Strings File

![Strings File](https://supergithuber.github.io/img2/multiLanguage_2.png)

文件名必须叫做 ***InfoPlist*** 

然后选中生成的***InfoPlist.strings***文件，在右侧的File Inspector的Localization选项中

![Localization](https://supergithuber.github.io/img2/multiLanguage_3.png)

选择其中一种语言，然后为剩下的打上勾，最后的结果如图

![result](https://supergithuber.github.io/img2/multiLanguage_4.png)

这个时候左边的InfoPlist.strings文件就出现一个三角尖，并且可以展开如下图

![result](https://supergithuber.github.io/img2/multiLanguage_5.png)

点击展开里面的文件，为每个文件写上一个字典，其中字典的key=CFBundleDisplayName，意思就是APP名字

```
///在简体中文的文件中
CFBundleDisplayName = "中文名";

///在英文的文件中
CFBundleDisplayName = "English Name";

///在法语的文件中
CFBundleDisplayName = "français Nom";

```
这个时候，在不同语言的iOS系统中，就可以看到APP显示不同的名字的了。
### 2. <span id="second">代码中字符串的本地化</span>

步骤有些类似，做个简化：

1. 新建一个Strings File文件，取名***Localizable***
2. 在***File inspection***的***Localization***菜单中，勾选响应的语言
3. 在对应语言的Strings File中写上你需要对应的Key-Value

```
///在简体中文的文件中
"button" = "按钮";

///在英文的文件中
"button" = "button";

///在法语的文件中
"button" = "Bouton";
```

那么在你需要调用的地方，调用**NSLocalizedString(key, comment)**这个函数就可以通过key来取得在不同语言系统下需要显示的文字，这是系统为我们定义好的一个宏

```objc
#define NSLocalizedString(key, comment) \
	    [NSBundle.mainBundle localizedStringForKey:(key) value:@"" table:nil]
```

看到这个你应该知道为什么文件名一定要是我们说的那个了。

比如我设置一个button的title，我就可以这么调用

```objc
[self.myButton setTitle:NSLocalizedString(@"button", nil) forState:UIControlStateNormal];
```

* 系统依据给定的key去响应的文件中搜索对应的value显示出来，如果没有找到，就把key作为value返回。通常情况下，英文文件中的的key和value是一样的，我们也可以省略它

### 3. <span id="third">多人开发中，私人本地化字符串表</span>

* 在多人开发中，我们有的时候不希望别人去动我们自己的本地化文件，即这份本地化文件只为我们一个人服务。
* 其实**NSLocalizedString(key, comment)**这个函数是去搜寻名字为**Localizable**的本地化文件。
* 如果需要有自己的本地化文件，我们可以取名为**XXX**，然后在调用的时候，用另一个宏，**NSLocalizedStringFromTable(key, tbl, comment)**，其中的tbl参数就是我们自己取的文件名。

例如我设置按钮名字，可以这么调用

```objc
[self.myButton setTitle:NSLocalizedStringFromTable(@"button", @"XXX", nil) forState:UIControlStateNormal];
```

### 4. <span id="fourth">图片本地化</span>

1. 本地化图片可以采用上面的方式，在本地化文件中配置上在不同语言下的，不同的文件名，然后通过宏来获取不同的文件名value，最后就生成了不一样的图片。这种方式是把不同的图片，都放在了相同的Assets中，管理起来还不太方便。
2. 第二种方法是先把图片拖到工程中（不是Assets.xcassets中）,同样点击右侧的File Inspector的Localization菜单中

结果如下图

![result](https://supergithuber.github.io/img2/multiLanguage_6.png)

对着每个语言对应的图片文件，Show in Finder，并在磁盘中替换为自己需要在不同语言环境下显示的图片，不同语言环境下，文件的名字要相同。

![result](https://supergithuber.github.io/img2/multiLanguage_7.png)

在调用的时候就可以获取到不同的文件了，例如我设置图片就可以这么调用

```objc
[self.myImageView setImage:[UIImage imageNamed:NSLocalizedString(@"hehe", nil)]];
```

### 5. <span id="fifth">本地化初始加载的一些知识</span>

* 程序在启动的时候，会去**standardUserDefaults**中读取key为**AppleLanguages**的value，这个value是一个string数组，它的firstobject为当前系统的语言，我们可以像下面这样获取当前系统的语言

```objc
NSArray *languages = [[NSUserDefaults standardUserDefaults] valueForKey:@"AppleLanguages"];
NSString *currentLanguage = languages.firstObject;
NSLog(@"模拟器当前语言：%@",currentLanguage);
```

* 因此我们可以在程序启动的时候，修改**standardUserDefaults**中key为**AppleLanguages**的数组的第一个值来让程序以为我们的语言环境是我们修改的那个，达到模拟语言环境的目的，而不用每次都去切换语言来检验

```objc
    // 切换语言前
    NSArray *langArr1 = [[NSUserDefaults standardUserDefaults] valueForKey:@"AppleLanguages"];
    NSString *language1 = langArr1.firstObject;
    NSLog(@"模拟器语言切换之前：%@",language1);
 
    // 切换语言
    NSArray *lans = @[@"en"];
    [[NSUserDefaults standardUserDefaults] setObject:lans forKey:@"AppleLanguages"];
 
    // 切换语言后
    NSArray *langArr2 = [[NSUserDefaults standardUserDefaults] valueForKey:@"AppleLanguages"];
    NSString *language2 = langArr2.firstObject;
    NSLog(@"模拟器语言切换之后：%@",language2);
```

附上一张多语言和它在iOS中的缩写对照表

![result](https://supergithuber.github.io/img2/multiLanguage_8.png)

* 在多语言中，不同的语言长短不一样，固定长度的UILabel可能导致显示不全的问题，需要把UILabel的adjustsFontSizeToFitWidth属性设置为YES，让它为我们调整文字的大小。