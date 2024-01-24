import os
import re
import glob

def read_txt_file(txt_file: str, key: str):
        '''txtファイルからディレクトリのパスを読み込む
        args:
            file_path: txtファイルのパス
            key: 取得したい値のkey
        examples:
            >>> read_txt_file('dir_path.txt', 'webui')
            'D:\stable-diffusion-webui\'
        '''
        with open(txt_file, 'r', encoding='UTF-8') as file:
            data = file.read()
            # {key}="この部分"を取得する
            pattern = re.compile(fr'{key}="(.*?)"')

            # マッチングを実行
            match = pattern.search(data)

            # マッチした文字列を取得
            if match:
                return match.group(1)
            else:
                return None


def fetch_latest_file(dir_path):
    '''最新のファイルを取得する'''
    # 指定のディレクトリ内にある全てのファイルをリストで取得
    files = glob.glob(os.path.join(dir_path, '*'))
    return max(files, key=os.path.getctime)