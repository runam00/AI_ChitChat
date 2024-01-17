import os
import tempfile
import shutil

import customtkinter as ct
import tkinter as tk
from PIL import Image

from .frames.top_page_frame import TopPageFrame
from .frames.chat_page_frame import ChatPageFrame
from .frames.sidebar_frame import SidebarFrame
from .states.frame_state import FrameState
from .theme.strings import UIString
from .theme.colors import BrandColor

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self._temp_dir = None  # 一時フォルダのパス
        self._generated_image = None  # 生成された画像のパス
        self._generated_audio_data = None  # 生成された音声ファイルのパス
        self._generated_video = None  # 生成されたトーキングフォト動画のパス
        self._messages_list: list[dict[str: str]] = []  # チャットの履歴 {'role': '','content': ''}

        self._frame_state = FrameState()  # フレームに関する状態を管理する
        self._frame_state.current_mainframe = UIString.TOP  # 初期値はトップページ

        ###モック###
        self._generated_video = 'assets/sample/sample.mp4'
        self._messages_list = [
            {'role': 'user', 'content': '1回目のメッセージ'},
            {'role': 'AI', 'content': 'プログラミング言語や使用しているフレームワークやライブラリによって異なりますが、一般的には「fetchLatestMessage」や「getLatestMessage」などのような関数名が使われることがあります。ただし、具体的なコンテキストや使用している技術によって最適な関数名が変わる可能性があります。'},
            {'role': 'user', 'content': '3回目のメッセージ'},
            {'role': 'AI', 'content': 'こんにちは、良い天気ですね'},
        ]
        ###

        # UIを表示
        self.build_ui()
        # 起動時にトップページを表示
        self.show_frame(UIString.TOP)
        # 指定したウィジェット以外の場所をクリックした際、フォーカスを外すためのイベントを設定
        self.bind('<Button-1>', self.remove_focus)
        # 一時フォルダを作成
        self.make_temp_dir()
        # プログラム終了時に一時ファイルを削除
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def build_ui(self):

        self.title('AI_ChitChat')
        self.geometry('1440x810')
        self.minsize(1440, 810)
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
        self._frame_state.mainframes = {
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
                root=self,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            )
        }
        # メインフレームを全て設置する
        for frame in self._frame_state.mainframes.values():
            frame.grid(row=0, column=0, sticky='nsew')

    def get_current_mainframe_name(self):
        '''現在表示されているメインフレームの名前を返す'''
        return self._frame_state.current_mainframe

    def update_current_mainframe_name(self, new_current_mainframe: str):
        '''現在表示しているフレームの情報を更新する'''
        self._frame_state.current_mainframe = new_current_mainframe

    def show_frame(self, frame_name: str):
        '''引数で指定されたフレームを一番上に表示する'''
        frame = self._frame_state.mainframes[frame_name]
        frame.tkraise()

    def get_generated_image(self):
        '''生成された画像オブジェクトを取得する'''
        ### モック ###
        self._generated_image = Image.open('assets/images/monster08.png')
        #######
        return self._generated_image

    def get_messages_list(self):
        '''全てのメッセージリストを取得する'''
        return self._messages_list

    def add_message(self, role, content):
        '''メッセージリストにメッセージを追加する'''
        self._messages_list.append({'role': role, 'content': content})

    def get_generated_video(self):
        '''生成された動画のパスを返す'''
        return self._generated_video

    def remove_focus(self, event):
        '''クリックした場所が指定されたウィジェットではない場合、フォーカスを外す'''
        # フォーカスを外したいウィジェットの型
        widget_types = [tk.Text, tk.Entry, tk.Label, ct.CTkCanvas]
        if type(event.widget) not in widget_types:
            event.widget.master.focus_set()

    def make_temp_dir(self):
        '''一時フォルダを作成'''
        self._temp_dir = tempfile.mkdtemp()
        ### デバッグ ###
        print(f'一時ファイルパス：{self._temp_dir}')
        ###

    def delete_temp_file(self):
        '''一時フォルダを削除'''
        if self._temp_dir is not None:
            shutil.rmtree(self._temp_dir)
            ### デバッグ ###
            print('一時フォルダ削除')
            folder_exists = os.path.exists(self._temp_dir)
            print(f"一時フォルダが存在するかどうか: {folder_exists}")
            ###

    def close_window(self):
        '''「×」ボタンが押された際にウィンドウを閉じる'''
        # 一時ファイルを削除する
        self.delete_temp_file()
        # プログラムを終了
        self.destroy()
        self.quit()