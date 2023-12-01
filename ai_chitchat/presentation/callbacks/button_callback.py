def sidebar_button_callback(master, selected):
    # ボタンの状態を更新
    button_state = master.button_state
    button_state.update_selected(selected)

    # 画面遷移
    master.show_mainframe(selected)