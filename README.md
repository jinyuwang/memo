memo
====
由于个人精力有限的原因，个人主要精力花在FeelUOwn这个项目上，如果哪位对这个项目有兴趣可以跟我联系，我可以提供一些力所能及的帮助。我觉得这东西还是挺有意义的。

注：本项目已经很久没有进行更新了。如果没人愿意接手的话，它可能一直都不会更新了。

__version 1.0__

正在进行version2.0的开发

## 介绍

一个轻量的便签软件

## 支持平台说明

__基本运行环境__

python2.7 pyqt4

__window linux 均可运行__

_附加说明_

1. windows下，程序支持热键 `\``,（需要从hotkey.py运行程序）
2. 也可以直接运行widget.py （不附带热键功能）

## 项目说明
- `exe.py` 支持windows下，把程序打包成exe
- `memo.sh` 支持bash，sh运行

--------------

欢迎提出建议和改进方案

- author : ysw    (zjuysw)
- email : yinshaowen241 [at] gmail [dot] com



# memo 2.0 设计文档(目标)

## 设计目标
1. 做一个插件模块(考虑到之前windows上存在一些快捷键，但是不跨平台的问题。还有打算开发一些针对特定平台的插件，所以尽量能分离出这样一个模块)
2. 程序可以被其他人读懂。
  > 这就要求有相应的文档，变量和信号的发射都要在相应的文档中记录下来。

3. 

## 基本需求分析
### 文字描述
1. 实现可以切换文字背景和前景颜色
2. 时间是中文
3. 置顶功能

### 基本设计图
![](./2.0/doc/preview.png)


## 程序架构 (不确定)
`dataAccess.py`: 负责读取json文件和把json保存进入文件
`showLabel.py`: 显示 标题|时间|详细内容
`edit.py`: 编辑功能
`message.py`: 处理消息

### 程序编写注意的地方
1. 发射信号的地方，需要记录     
2. 类成员变量和函数

3. 编写一个dev环境用于开发时的测试之类

## API接口

