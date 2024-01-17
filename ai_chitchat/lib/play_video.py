def play_video(frame):
    root = frame.get_root()  # Appクラス
    video_player = frame.get_video_player()  # ビデオプレイヤー

    video = root.get_generated_video()  # 動画のパス
    audio = root.get_generated_audio()  # 音声ファイルのパス

    ### デバッグ ###
    print(video)
    ###

    # 動画を読み込む
    video_player.load(video, audio)

    # 動画を再生
    video_player.start()