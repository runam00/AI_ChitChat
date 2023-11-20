import customtkinter

from .sidebar_frame import SidebarFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('AI_ChitChat')
        self.geometry('1200x600')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = SidebarFrame(self)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
