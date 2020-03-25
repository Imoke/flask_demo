https://code.visualstudio.com/docs/python/python-tutorial

1.安装虚拟环境

```
# macOS/Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv env
# Windows
python -m venv env
```

In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Select Interpreter command

2.安装需要的包

`pip install -r requirements.txt`

3.运行程序

`gunicorn hello_app.webapp:app -c gunicorn.conf.py`

4.打包镜像
`pip freeze > requirements.txt`
`sudo docker build -t 'flask_app' .`

5.运行镜像

`docker run -p 9006:9006 flask_app`