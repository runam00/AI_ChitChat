from ai_chitchat.lib.generate_video import run_command

def test_run_command_with_echo():
    '''echoコマンドを入力すると、終了ステータスが0で引数に指定した文字列が出力される'''
    sentence = 'Hello, World'
    command = ['echo', sentence]
    result = run_command(command)
    assert result.returncode == 0
    assert result.stdout == sentence