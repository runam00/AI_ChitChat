def generate_image(frame):
    root = frame.get_root()
    frame_generate = frame.get_frame_generate()  # 画像生成フレーム（未生成）
    frame_generated_image = frame.get_frame_generated_image()  # 画像生成済みフレーム

    # 画像生成の際に渡すユーザーテキストを取得する
    user_text = frame_generate.get_user_text()

    # 画像生成済みフレームに遷移
    frame_generate.pack_forget()
    frame_generated_image.pack(expand=True)

    # 生成された画像を表示
    generated_image = root.get_generated_image()
    # generated_image = generated_image.resize((ImageSize.WIDTH, ImageSize.HEIGHT))
    frame_generated_image.update_generated_image(generated_image)