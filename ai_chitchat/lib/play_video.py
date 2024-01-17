def play_video(frame):
    root = frame.get_root()  # Appクラス
    video_player = frame.get_video_player()  # ビデオプレイヤー

    path = root.get_generated_video()  # 動画のパス

    ### デバッグ ###
    print(path)
    ###

    # 動画を読み込む
    video_player.load(path)

    # 動画を再生
    video_player.start()