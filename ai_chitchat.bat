@echo off

cd /d %~dp0
python -m venv .venv

call .venv\Scripts\activate

pip install -r requirements.txt

python ai_chitchat/main.py

deactivate