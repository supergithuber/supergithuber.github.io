## Git别名

配置别名，就是缩写了。

> git status

太长，可以修改git全局配置让命令变成

> git st

经常要配置，忘了，总结下

> git config --global alias.st status
> 
> git config --global alias.co checkout
> 
> git config --global alias.ci commit
> 
> git config --global alias.br branch
> 
> git config --global alias.last 'log -1'
> 

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"


配置完的信息都在.gitconfig文件中。

github的markdown解释器把双横线解释为单横线，这里需要复制完修改一下。