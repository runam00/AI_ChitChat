import customtkinter as ct

from ..theme.strings import UIString

class TopPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×3でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text=UIString.TITLE)
        self.label.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

        # タブ
        self.tabs = ct.CTkTabview(master=self)
        self.tabs.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')

        self.tabs.add(UIString.GENERATE)
        self.tabs.add(UIString.TAB_GALLERY)

        # 画面遷移で使用するフレームの辞書
        self.generate_tab_frames: dict[str, ct.CTkFrame] = {}

        # 「作成」タブ内のフレーム
        self.generate_tab = GenerateTabFrame(parent=self.tabs.tab(UIString.GENERATE))
        self.generate_tab_frames['not generated'] = self.generate_tab
        # 「作成」タブ内で、生成された画像で決定するか確認するフレーム
        self.generate_confirmation_tab = GenerateTabConfirmationFrame(parent=self.tabs.tab(UIString.GENERATE))
        self.generate_tab_frames['generated'] = self.generate_confirmation_tab


class GenerateTabFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×2でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # テキストボックス
        self.text_box = ct.CTkTextbox(master=self)
        self.text_box.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        
        # 生成ボタン
        self.button = ct.CTkButton(master=self)
        self.button.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')


class GenerateTabConfirmationFrame(ct.ctk_tk):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×2でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


class GalleryTabFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×2でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


class TabButton(ct.CTkButton):
    def __init__(self, parent, text, callback, **kwargs):
        super().__init__(parent, **kwargs)
        self.button = ct.CTkButton(
            master=self,
        )
        self.button.pack()