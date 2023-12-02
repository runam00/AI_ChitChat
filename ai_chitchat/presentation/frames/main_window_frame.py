import customtkinter as ct

from .sidebar_frame import SidebarFrame
from ..theme.colors import BrandColor

class MainWindowFrame(ct.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # 全体のレイアウトを設定
        self.setup_layout()


    def setup_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        # サイドバー設置用スペース
        self.sidebar_frame = ct.CTkFrame(master=self, width=100)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム設置用スペース
        self.mainframe = ct.CTkFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

        # サイドバーのフレームを設置
        self.sidebar_view = SidebarFrame(parent=self.sidebar_frame, fg_color=BrandColor.DARK_GRAY)
        self.sidebar_view.pack(
            # TODO
        )