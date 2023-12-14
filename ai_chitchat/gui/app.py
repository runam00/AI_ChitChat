import customtkinter as ct
import tkinter as tk
from PIL import Image, ImageTk

from .frames.top_page_frame import TopPageFrame
from .frames.chat_page_frame import ChatPageFrame
from .frames.sidebar_frame import SidebarFrame
from .states.frame_state import FrameState
from .theme.strings import UIString
from .theme.colors import BrandColor
from .theme.sizes import ImageSize

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        
        self.frame_state = FrameState()  # フレームに関する状態を管理する
        self.frame_state.current_mainframe = UIString.TOP  # 初期値はトップページ
        self.generated_image = None  # 生成された画像

        # UIを表示
        self.build_ui()
        # 起動時にトップページを表示
        self.show_frame(UIString.TOP)


    def build_ui(self):
        self.title('AI_ChitChat')
        self.geometry('1280x720')
        ct.set_appearance_mode("dark")

        # 2×1でグリッドを設定
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # サイドバー設置用スペース
        self.sidebar_area = ct.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_area.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム設置用スペース
        self.mainframe_area = ct.CTkFrame(self, corner_radius=0)
        self.mainframe_area.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')
        self.mainframe_area.columnconfigure(0, weight=1)
        self.mainframe_area.rowconfigure(0, weight=1)

        # サイドバーのフレームを設置
        self.sidebar_frame = SidebarFrame(
            root=self,
            parent=self.sidebar_area,
            fg_color=BrandColor.DARK_GRAY,
            corner_radius=0
        )
        self.sidebar_frame.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)

        # メインフレームを生成
        self.frame_state.mainframes = {
            # トップページのメインフレーム
            UIString.TOP: TopPageFrame(
                parent=self.mainframe_area,
                root=self,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            ), 
            # チャットページのメインフレーム
            UIString.CHAT: ChatPageFrame(
                parent=self.mainframe_area,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            )
        }
        # メインフレームを全て設置する
        for frame in self.frame_state.mainframes.values():
            frame.grid(row=0, column=0, sticky='nsew')


    def get_current_mainframe_name(self):
        '''現在表示されているメインフレームの名前を返す'''
        return self.frame_state.current_mainframe


    def update_current_mainframe_name(self, new_current_mainframe: str):
        '''現在表示しているフレームの情報を更新する'''
        self.frame_state.current_mainframe = new_current_mainframe


    def show_frame(self, frame_name: str):
        '''引数で指定されたフレームを表示する'''
        frame = self.frame_state.mainframes[frame_name]
        frame.tkraise()


    def get_generated_image(self):
        ### モック ###
        img = Image.open('assets/images/monster07.png')
        img = img.resize((ImageSize.WIDTH, ImageSize.HEIGHT))
        self.generated_image = ImageTk.PhotoImage(img)
        #######
        return self.generated_image