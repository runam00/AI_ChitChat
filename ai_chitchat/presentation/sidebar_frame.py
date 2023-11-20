import customtkinter

class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # TODO 文言の文字列
        self.button_home = customtkinter.CTkButton(self, text='1')
        self.button_home.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.button_chat = customtkinter.CTkButton(self, text='2')
        self.button_chat.grid(row=1, column=0, padx=10, pady=10, sticky='ew')