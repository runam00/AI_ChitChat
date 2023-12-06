import customtkinter as ct

from ..theme.strings import UIString
from ..theme.colors import BrandColor
from ..theme.sizes import TopFrameSize
from ..theme.fonts import TopFrameFont

class TopPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×3でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)

        # アプリタイトル
        self.label = ct.CTkLabel(
            self,
            text=UIString.TITLE,
            font=TopFrameFont.TITLE,
            text_color=BrandColor.WHITE
        )
        self.label.grid(row=0, column=0, padx=0, pady=(110, 50))

        # タブ
        self.tabs = ct.CTkTabview(
            self,
            width=TopFrameSize.TAB_WIDTH,
            fg_color=BrandColor.GRAY,
            segmented_button_fg_color=BrandColor.GRAY,
            segmented_button_selected_color=BrandColor.BLUE,
            segmented_button_selected_hover_color=BrandColor.BLUE,
            segmented_button_unselected_color=BrandColor.DARK_GRAY,
            segmented_button_unselected_hover_color=BrandColor.BLUE,
            text_color=BrandColor.WHITE,
        )
        self.tabs._segmented_button.configure(font=TopFrameFont.TAB_BUTTON)
        self.tabs.grid(row=1, column=0, padx=0, pady=0)
        self.tabs.add(UIString.TAB_GENERATE)  # 作成タブ
        self.tabs.add(UIString.TAB_GALLERY)  # ギャラリータブ

        # [作成]説明文
        self.description = ct.CTkLabel(
            self.tabs.tab(UIString.TAB_GENERATE),
            text_color=BrandColor.LIGHT_GRAY,
            text=UIString.GENERATE_DESCRIPTION,
            font=TopFrameFont.DESCRIPTION
        )
        self.description.grid(row=0, column=0, padx=0, pady=(10, 15))

        # [作成]テキストボックス
        self.text_box = ct.CTkTextbox(
            self.tabs.tab(UIString.TAB_GENERATE),
            width=TopFrameSize.TEXT_BOX_WIDTH,
            height=TopFrameSize.TEXT_BOX_HEIGHT,
            padx = 12,
            pady = 8,
            fg_color=BrandColor.DARK_GRAY,
            text_color=BrandColor.WHITE,
            font=TopFrameFont.TEXT_BOX
        )
        self.text_box.grid(row=1, column=0, padx=0, pady=(0, 0))

        # ボタン
        self.button = ct.CTkButton(
            self,
            width=TopFrameSize.BUTTON_WIDTH,
            height=TopFrameSize.BUTTON_HEIGHT,
            font=TopFrameFont.BUTTON,
            fg_color=BrandColor.BLUE
        )
        self.button.grid(row=2, column=0, padx=0, pady=(20, 60))


class GenerateTabFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×2でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # テキストボックス
        self.text_box = ct.CTkTextbox(self)
        self.text_box.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


class GalleryTabFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.button = ct.CTkButton(self, text='決定')
        self.button.grid(row=0, column=0)