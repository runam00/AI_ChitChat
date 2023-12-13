import customtkinter as ct

class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)


class InterfaceFrame(ct.CTkFrame):
    '''テキスト送信、音量調整、ダウンロードなどのユーザーインターフェースを配置するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)


class ChatHistoryFrame(ct.CTkFrame):
    '''チャット履歴を表示するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)