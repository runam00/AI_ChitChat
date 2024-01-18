import os
import subprocess

def generate_video(frame):
    root = frame.get_root()  # Appクラス
    app_path = root.get_ai_chitchat_dir()
    image = root.get_image_path()  # 画像ファイル(png)
    image = os.path.join(app_path, image)
    audio = root.get_generated_audio()  # 音声ファイル(wav)
    audio = os.path.join(app_path, audio)
    cwd = root.get_sadtalker_dir()  # sadtalkerがあるディレクトリ

    result = run_sadtalker(image, audio, cwd)
    print(result.stdout)

def run_command(command: list, cwd=None):
    '''
    シェルコマンドを実行する
    args:
        command: シェルコマンド
        cwd: 実行するディレクトリ
    '''
    try:
        return subprocess.run(command, cwd=cwd, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_sadtalker(image, audio, cwd):
    # sadtalkerのコマンド
    command = [
        "python",
        "inference.py",
        "--driven_audio",
        audio,
        "--source_image",
        image,
        "--enhancer",
        "gfpgan"
    ]
    # 動画を生成する
    return run_command(command, cwd)