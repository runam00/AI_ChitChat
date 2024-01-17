import subprocess

def generate_video(frame):
    root = frame.get_root()  # Appクラス
    image = root.get_image_path()  # 画像ファイル(png)
    audio = root.get_generated_audio()  # 音声ファイル(wav)

    # 動画を生成する
    result = run_command([])
    print(result.stdout)

def run_command(command: list):
    '''シェルコマンドを実行する'''
    return subprocess.run(command, capture_output=True, text=True)