import customtkinter as ct

from .sidebar_frame import SidebarFrame

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title('AI_ChitChat')
        self.geometry('1200x600')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # サイドバー
        self.sidebar_frame = SidebarFrame(self, fg_color='#222831')
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
