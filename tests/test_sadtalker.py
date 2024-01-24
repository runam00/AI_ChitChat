import os
from ai_chitchat.lib.file_utils import read_txt_file
from ai_chitchat.infrastructure.sadtalker import run_sadtalker

def test_run_sadtalker():
    webui = read_txt_file('dir_path.txt', 'webui')
    sadtalker = r'extensions\SadTalker'  # webuiからsadtalkerまでのパス
    cwd = os.path.join(webui, sadtalker)
    image = os.path.join(cwd, r'examples\source_image\art_18.png')
    audio = os.path.join(cwd, r'examples\driven_audio\bus_chinese.wav')
    venv_python = os.path.join(os.getcwd(), r'.venv\Scripts\python.exe')
    run_sadtalker(image, audio, cwd, venv_python)