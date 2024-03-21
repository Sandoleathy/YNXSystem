@echo off

REM 设置虚拟环境（仅在需要时）
if not exist venv (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
venv\Scripts\activate

REM 安装依赖项
echo 安装依赖项...
pip install -r requirements.txt

REM 设置 Flask 应用程序
set FLASK_APP=your_application.py

REM 启动 Flask 应用程序
echo 启动 Flask 应用程序...
flask run
