import customtkinter

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # TODO 文言の文字列
        # アプリタイトル
        self.label = customtkinter.CTkLabel(self, text='AI ChitChat')