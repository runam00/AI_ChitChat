

def add_chat_message(root, chat_history_frame, role: str, text: str):
    # appクラスのメッセージリストに追加
    root.add_message(role, text)
    # 最新のメッセージを配置
    message_list = root.get_messages_list()
    chat_history_frame.place_message(message_list[-1], len(message_list)-1)