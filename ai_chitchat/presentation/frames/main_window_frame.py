import customtkinter as ct

from .sidebar_frame import SidebarFrame
from .top_page_frame import TopPageFrame
from .chat_page_frame import ChatPageFrame
from ..theme.colors import BrandColor
from ..theme.strings import UIString

class MainWindowFrame(ct.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # 全体のレイアウトを設定
        self.setup_layout()
        self.init_mainframes()


    def setup_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        # サイドバー設置用スペース
        self.sidebar_frame = ct.CTkFrame(master=self, width=100)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム設置用スペース
        self.mainframe = ct.CTkFrame(master=self)
        self.sidebar_frame.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')

        # サイドバーのフレームを設置
        self.sidebar_view = SidebarFrame(master=self.master, parent=self.sidebar_frame, fg_color=BrandColor.DARK_GRAY)
        self.sidebar_view.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


    def init_mainframes(self):
        self.top_page_frame = TopPageFrame(parent=self)
        self.chat_page_frame = ChatPageFrame(parent=self)
        self._mainframe_list = {
            UIString.TOP: self.top_page_frame, 
            UIString.CHAT: self.chat_page_frame
        }


    def get_mainframes(self) -> list:
        return self._mainframe_list