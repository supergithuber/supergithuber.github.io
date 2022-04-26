## pyenv无法修改Python --version显示的版本

在Mac上

如果安装了oh my zsh，就在 `~/.zshrc`中新增，否则就在`~/.bashrc`中新增：

```shell
export PYENV_ROOT=/Users/wuxi/.pyenv  # pyenv 的安装路径，各电脑会有所不同
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
```

并在`~/.bashrc`中新增：

```shell
export PYENV_ROOT=~/.pyenv
export PATH=$PYENV_ROOT/shims:$PATH
```

之后 `source ~/.zshrc`或者`source ~/.bashrc`，或者重启命令行工具
