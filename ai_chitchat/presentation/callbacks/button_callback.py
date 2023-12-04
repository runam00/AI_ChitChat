import customtkinter as ct

def sidebar_button_callback(parent_frame, master, selected: str):
    # ボタンの状態を更新
    button_state = master.get_button_state()
    button_state.update_selected(selected)

    # ボタンの色を更新
    parent_frame.set_buttons_color()

    # 画面遷移
    master.change_mainframe(frame_name=selected)