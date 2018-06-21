## Mac下python路径

1. Mac系统自带python路径为／System／Library／Frameworks／Python.framework/Version 这里可能会有多个python版本，里面Current存放系统当前python版本，进入Current／bin，在终端输入./python --version即可查看系统当前python版本（注：若使用python --version命令是查看用户当前python版本而不是系统python版本）。

2. HomeBrew安装python路径为／usr/local/Cellar/python 里面存放HomeBrew所安装版本，进入2.7.13/bin，在终端输入./python --version 即可查看用户当前使用的python版本。如果使用brew工具正确安装python的情况下，用户当前python版本会是新安装的python。

3. 系统命令默认路径在／usr／bin，用户命令默认路径在／usr／local／bin（brew安装的命令默认在这个路径下） 。如果存在相同的命令，则会依据／etc／paths 文件中的环境变量顺序（前面优先于后面）依次查找，查看环境变量也可以在终端输入echo $PATH 查看，遵循左面路径优先于右面路径。