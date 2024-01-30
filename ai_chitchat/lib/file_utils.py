import os
import re
import glob
import datetime

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


def generate_filename(prefix, extension):
    '''
    現在時刻からファイル名を生成する
    args:
        prefix: 先頭につける文字
        extension: 拡張子('.txt'など）
    '''
    # 西暦(4桁)月(2桁)日(2桁)_時(2桁)分(2桁) 例:20240130_0850
    current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    return f'{prefix}_{current_time}{extension}'