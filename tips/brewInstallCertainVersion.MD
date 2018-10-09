## homebrew安装指定版本软件

今天把carthage更新到0.31.0，发现不支持版本号为4位的库（1.3.2.3这样的），然后有些用到三方库还是四位的，不得已要降级carthage，如果本地已经有低版本的，可以直接通过命令切换降级:

```
carthage switch carthage 0.29.0
```

如果本地没有低版本的，就要安装线上的低版本。

* brew通过git管理一些软件的版本信息去拉取对应的软件，所以可以通过以下命令查看brew源的地址

```
brew info carthage
```

可以看到以下信息:

```
carthage: stable 0.31.0 (bottled), HEAD
Decentralized dependency manager for Cocoa
https://github.com/Carthage/Carthage
/usr/local/Cellar/carthage/0.29.0 (69 files, 26.7MB)
  Poured from bottle on 2018-04-18 at 17:48:01
/usr/local/Cellar/carthage/0.31.0 (69 files, 25.2MB) *
  Poured from bottle on 2018-10-09 at 10:26:18
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/carthage.rb
==> Requirements
Build: xcode ✔
==> Options
--HEAD
	Install HEAD version
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Analytics
install: 28,960 (30d), 76,177 (90d), 286,220 (365d)
install_on_request: 27,791 (30d), 71,774 (90d), 256,872 (365d)
build_error: 1,039 (30d)
```

可以找到brew源的地址是:[https://github.com/Homebrew/homebrew-core/blob/master/Formula/carthage.rb](https://github.com/Homebrew/homebrew-core/blob/master/Formula/carthage.rb)

我们每次执行brew upgrade carthage这种命令更新软件的时候，它就是去拉取homebrew最新的版本，然后用对应软件的最新rb文件内的信息来更新。

所以我把整个homebrew在git上的库拉下来

```
git clone git@github.com:Homebrew/homebrew-core.git
```

找到对应文件的git log信息

```
git log ./Formula/carthage.rb | less
```

```
commit 6dbf905c3b6726d6f68c7d265f876e2c5668adba
Author: BrewTestBot <homebrew-test-bot@lists.sfconservancy.org>
Date:   Tue Oct 2 04:18:29 2018 +0000

    carthage: update 0.31.0 bottle.

commit aed3552ab30d5dfb430cd4034f674d05dc01d56c
Author: J.D. Healy <jdhealy@gmail.com>
Date:   Tue Sep 25 01:08:22 2018 +0200

    carthage 0.31.0

    Closes #32544.

    Signed-off-by: FX Coudert <fxcoudert@gmail.com>

commit 2f937f76413acfe459c75586ec1214d5797198fa
Author: BrewTestBot <brew-test-bot@googlegroups.com>
Date:   Mon Jul 2 14:12:34 2018 +0000

    carthage: update 0.30.1 bottle.

commit 492753d624052feb403b6123fd852f817a809294
Author: ilovezfs <ilovezfs@icloud.com>
Date:   Mon Jul 2 07:04:06 2018 -0700

    carthage 0.30.1

    Closes #29658.

    Signed-off-by: ilovezfs <ilovezfs@icloud.com>

commit 45dd24d8dfa7a2fb69812c678ceb34be0c16e295
Author: BrewTestBot <brew-test-bot@googlegroups.com>
Date:   Tue Mar 20 08:58:42 2018 +0000

    carthage: update 0.29.0 bottle.

```

找到0.29.0对应的commit是：45dd24d8dfa7a2fb69812c678ceb34be0c16e295

切到对应的commit

```
git checkout 45dd24d
```

此时可以打开 ./Formula/carthage.rb 文件发现已经显示的是0.29.0的版本信息和下载地址

然后利用这个文件来安装

```
brew install ./Formula/carthage.rb
```

完成安装对应版本的carthage。