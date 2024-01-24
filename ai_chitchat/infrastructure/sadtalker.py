import subprocess

def run_sadtalker(image, audio, cwd, venv_python):
    '''
    sadtalkerを実行して動画を生成する
    args:
        image: 生成する動画の元になる画像のパス
        audio: 生成する動画の元になる音声のパス
        cwd: sadtalkerが存在するパス
        venv: ai_chitchatのrequirements.txtをpipインストールした仮想環境に存在するpython.exeのパス
    '''
    # sadtalkerのコマンド
    command = [
        venv_python,
        'inference.py',
        '--driven_audio',
        audio,
        '--source_image',
        image,
        '--enhancer',
        'gfpgan'
    ]
    # 動画を生成する
    run_command(command, cwd)

def run_command(command: list, cwd=None):
    '''
    シェルコマンドを実行する
    args:
        command: シェルコマンド
        cwd: 実行するディレクトリ
    '''
    proc = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    # コマンドの標準出力を取得
    while True:
        line = proc.stdout.readline()
        if line:
            print(line.decode('utf8', 'replace').strip())
        if not line and proc.poll() is not None:
            break

    # プロセスの終了を待機
    proc.wait()