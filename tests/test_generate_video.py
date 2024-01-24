import os
from ai_chitchat.lib.generate_video import run_command, run_sadtalker

def test_run_command_with_echo():
    '''echoコマンドを入力すると、終了ステータスが0で引数に指定した文字列が出力される'''
    sentence = 'Hello, World'
    command = ['echo', sentence]

    result = run_command(command)
    print(f'結果：{result}')
    assert result.returncode == 0
    assert result.stdout.strip('"\n') == sentence

def test_run_command_execution_location():
    '''期待通りの場所でシェルコマンドが実行される'''
    test_file = 'test.txt'
    command = ['echo', '.', '>', test_file]
    cwd = '../AI_ChitChat_tool/'
    result = run_command(command, cwd)

    expected_location = cwd
    actual_location = result.stdout.strip()
    # assert expected_location == actual_location

def test_run_sadtalker():
    '''sadtalkerを実行して動画ファイルが生成される'''
    image = '../../../AI_ChitChat/assets/sample/sample.png'
    audio = '../../../AI_ChitChat/assets/sample/sample.wav'
    cwd = '../AI_ChitChat_tool/sadtalker/SadTalker/'
    result = run_sadtalker(image, audio, cwd)
    print(f'結果：{result.stderr}')