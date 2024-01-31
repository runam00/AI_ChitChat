# AI ChitChat

1枚の画像と音声から作られるリップシンク動画を通して、好みのキャラクターとの会話を楽しめるアプリです。

_VOICEVOX:四国めたん_

## インストール

### Windows

1.  [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) をインストールし、パスを通します。
2. [git](https://git-scm.com/download/win) をインストールします。
3. [ffmpeg](https://ffmpeg.org/download.html) をダウンロードし、パスを通します。
4. [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)をダウンロードして解凍します。
5. 次のコマンドを実行してstable-diffusion-webuiをダウンロードします。 `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`
6. CIVITAIから[realcartoon-realistic](https://civitai.com/models/97744/realcartoon-realistic)というモデルをダウンロードし、フォルダ `stable-diffusion-webui\models\Stable-diffusion`下に置きます。
7. webuiを起動し、「extentions」→「install from URL」で次のURLを入力してインストールしてください。`https://github.com/Winfredy/SadTalker.git`
8. フォルダ`stable-diffusion-webui/extentions/SadTalker`下に`checkpoints`というフォルダを作成します。
9. [SadTalker](https://github.com/OpenTalker/SadTalker) の「Download Models」からモデルをダウンロードして展開し、先ほど作成したフォルダ`stable-diffusion-webui/extentions/SadTalker/checkpoints`下に中身を全て置きます。
10. Stable Diffusionの`webui-user.bat`をメモ帳などのエディタで開き、次の2文を追記します。
```
set SADTALKER_CHECKPOINTS="stable-diffusion-webui/extentions/SadTalker/checkpointsのパス"
set COMMANDLINE_ARGS=--api
```
11. 次のコマンドを実行してAI ChitChatリポジトリをダウンロードします。 `git clone https://github.com/runam00/AI_ChitChat.git`
12. `AI_ChitChat/dir_path.txt`をメモ帳などのエディタで開き、`webui="webuiのパス"`とwebuiのパスを追記してください。
13. PCの環境変数に`MIIBO_API_KEY`と`MIIBO_AGENT_ID`という変数名で、miiboのAPIキーを2つ登録します。

## 起動

1. `run.exe`でVOICEVOXを起動します。
2. `webui-user.bat`でstable-diffusion-webuiを起動します。
3. 上記2つの起動を確認したら、`ai_chitchat.bat`でAI ChitChatを起動します。