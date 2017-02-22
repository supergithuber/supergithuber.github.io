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

然后选中生成的***InfoPlist.strings***文件，在右侧的File Inspector的Localication选项中

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

### 3. <span id="third">多人开发中，私人本地化字符串表</span>

### 4. <span id="fourth">图片本地化</span>

### 5. <span id="fifth">本地化初始加载的一些知识</span>