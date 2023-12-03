def sidebar_button_callback(master, selected: str):
    # ボタンの状態を更新
    button_state = master.get_button_state()
    button_state.update_selected(selected)

    # 画面遷移
    mainframes = master.get_mainframes()
    master.change_mainframe(flame=mainframes[selected])