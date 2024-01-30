from gui.theme.strings import UIString
from infrastructure.chatbot import send_message_chatbot


def add_chat_message(frame):
    root = frame.get_root()  # Appクラス
    interface_frame = frame.get_interface_frame()
    history_frame = frame.get_chat_history_frame()

    user_text = interface_frame.get_user_text()
    place_message(root, history_frame, UIString.ROLE_USER, user_text)

    # 返答テキストを取得して配置
    response = send_message_chatbot(user_text)
    place_message(root, history_frame, UIString.ROLE_AI, response)

    # テキストボックスを空にする
    interface_frame.user_input_text_box.delete(0, 'end')

    return response

def place_message(root, history_frame, role, text):
    # appクラスのメッセージリストに追加
    root.add_message(role, text)
    # 最新のメッセージを配置
    message_list = root.get_messages_list()
    history_frame.place_message(message_list[-1], len(message_list)-1)