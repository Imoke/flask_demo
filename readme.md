# 项目 Setup

## 第一步：Install virtual env

```
# Windows
python -m venv env
```

## 第二步 进入虚拟环境（后面的命名都必须在虚拟环境的 shell 中进行）

vscode
ctrl+shift+p Python: Select Interpreter 选择当前 env 中的环境

vscdoe

```
ctrl + ~
```

window 注意必须是 cmd 不能 powershell

```
env\Scripts\activate.bat
```

Linux

```
source env/bin/activate
```

## 第三步 Install dependence

```
pip install -r requirements.txt
```

## 第四步（可选） Freeze dependence

在安装新的依赖后，必须冻结依赖并且提交 requirements.txt 到 git 中，以便其他同事同步安装此依赖

```
pip freeze > requirements.txt
```

## 第五步 Run app

Window

```
set FLASK_APP=package.run
py -m flask run
```

Linux

```
export set FLASK_APP=package.run
```
