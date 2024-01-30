import os
from infrastructure.sadtalker import run_sadtalker

def generate_video(frame):
    # Appクラス
    root = frame.get_root()
    app_path = root.get_ai_chitchat_dir()

    # 画像ファイル(png)
    image = root.get_image_path()
    image = os.path.join(app_path, image)

    # 音声ファイル(wav)
    audio = root.get_generated_audio()
    audio = os.path.join(app_path, audio)

    # sadtalker
    webui = root.get_webui_dir()  # webuiのパス
    sadtalker = 'extensions\SadTalker'  # webuiからsadtalkerまでのパス
    cwd = os.path.join(webui, sadtalker)  # sadtalkerがあるディレクトリ
    venv_python = os.path.join(app_path, '.venv\Scripts\python.exe')

    # sadtalkerを実行
    run_sadtalker(image, audio, cwd, venv_python)

    # 生成された動画のパスを取得
    root.fetch_generated_video()
    print('動画が生成されました')