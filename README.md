# oliver-codegen 
oliver-codegen 是一款快速构建项目基础框架的脚手架工具. 其原理是从 Github 下载对应模板到本地, 并没有什么魔法代码. 


## 安装
```bash
$ pipx install oliver-codegen
```


## 使用方式
```bash
$ codegen create your_project_name -t python
```
其中 `-t` 后的参数是选择什么模板创建项目. 查看支持哪些模板命令 `codegen list template`


## 展示配置
输入以下命令, 将在控制台展示支持哪些模板.
```bash
$ codegen list template
```


## 更新程序
```bash
$ pipx upgrade oliver-codegen
```


## 卸载程序
```bash
$ pipx uninstall oliver-codegen
```
