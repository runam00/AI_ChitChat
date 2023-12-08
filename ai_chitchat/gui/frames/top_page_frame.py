import customtkinter as ct
from PIL import Image

from ..theme.strings import UIString
from ..theme.colors import BrandColor
from ..theme.sizes import TopFrameSize
from ..theme.fonts import TopFrameFont
from ..theme.images import GalleryImagePath

class TopPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self._current_name: str = ''

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
        self.label.grid(row=0, column=0, padx=0, pady=(90, 40))

        # タブ
        self.tabs = ct.CTkTabview(
            self,
            width=TopFrameSize.TAB_WIDTH,
            height=TopFrameSize.TAB_HEIGHT,
            fg_color=BrandColor.GRAY,
            segmented_button_fg_color=BrandColor.DARK_GRAY,
            segmented_button_selected_color=BrandColor.BLUE,
            segmented_button_selected_hover_color=BrandColor.BLUE,
            segmented_button_unselected_color=BrandColor.DARK_GRAY,
            segmented_button_unselected_hover_color=BrandColor.BLUE,
            text_color=BrandColor.WHITE,
            command=lambda: self.button_callback(self.tabs)
        )
        self.tabs._segmented_button.configure(font=TopFrameFont.TAB_BUTTON)
        self.tabs.grid(row=1, column=0, padx=0, pady=0)
        self.tabs.add(UIString.TAB_GENERATE)
        self.tabs.add(UIString.TAB_GALLERY)

        # タブボタンの横幅をスペースで調整
        self._tab_segmented_buttons_dict = self.tabs._segmented_button._buttons_dict
        self._tab_segmented_buttons_dict[UIString.TAB_GENERATE].configure(text=f'　　 {UIString.TAB_GENERATE} 　　')
        self._tab_segmented_buttons_dict[UIString.TAB_GALLERY].configure(text=f'　{UIString.TAB_GALLERY}　')

        # 作成タブ
        self.frame_generate = TabGenerateFrame(
            self.tabs.tab(UIString.TAB_GENERATE),
            fg_color=BrandColor.GRAY
        )
        self.frame_generate.pack(expand=True)
        # ギャラリータブ
        self.frame_gallery = TabGalleryFrame(
            self.tabs.tab(UIString.TAB_GALLERY),
            fg_color=BrandColor.GRAY
        )
        self.frame_gallery.pack(expand=True)

        # ボタン
        self.button = ct.CTkButton(
            self,
            text=UIString.GENERATE,
            width=TopFrameSize.BUTTON_WIDTH,
            height=TopFrameSize.BUTTON_HEIGHT,
            font=TopFrameFont.BUTTON,
            fg_color=BrandColor.BLUE
        )
        self.button.grid(row=2, column=0, padx=0, pady=(10, 30))


    def change_button_text(self):
        if self._current_name == UIString.TAB_GENERATE:
            self.button.configure(text=UIString.GENERATE)
        elif self._current_name == UIString.TAB_GALLERY:
            self.button.configure(text=UIString.SELECT_FROM_GALLERY)


    def button_callback(self, button):
        current_name: str = button.get()
        self._current_name = current_name.strip()
        self.change_button_text()


class TabGenerateFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 1×2でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # 説明文
        self.description = ct.CTkLabel(
            self,
            text_color=BrandColor.LIGHT_GRAY,
            text=UIString.GENERATE_DESCRIPTION,
            font=TopFrameFont.DESCRIPTION
        )
        self.description.grid(row=0, column=0, padx=0, pady=(0, 20))

        # テキストボックス
        self.text_box = ct.CTkTextbox(
            self,
            width=TopFrameSize.TEXT_BOX_WIDTH,
            height=TopFrameSize.TEXT_BOX_HEIGHT,
            padx= 12,
            pady= 8,
            fg_color=BrandColor.DARK_GRAY,
            text_color=BrandColor.WHITE,
            font=TopFrameFont.TEXT_BOX
        )
        self.text_box.grid(row=1, column=0, padx=0, pady=(0, 0))


class TabGalleryFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # 3×3でグリッドを設定
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # 2×3でオリジナル画像を表示する
        self.gallery_images = GalleryImagePath.get_values()
        self._images: list[ct.CTkButton] = []
        self._current_index = None
        self._count = 0
        for row in range(2):
            for col in range(3):
                image = ct.CTkImage(Image.open(self.gallery_images[self._count]), size=(100, 100))
                image_button = ct.CTkButton(
                    self,
                    width=110,
                    height=110,
                    text=None,
                    fg_color='transparent',
                    hover_color=BrandColor.BLUE,
                    image=image,
                    command=lambda i=self._count: self.button_callback(i)
                )
                self._images.append(image_button)
                image_button.grid(row=row, column=col, padx=7, pady=8)
                self._count += 1


    def change_images_color(self):
        '''現在選択している画像のみ枠を青くする'''
        for i in range(len(self._images)):
            if i == self._current_index:
                self._images[i].configure(fg_color=BrandColor.BLUE)
            else:
                self._images[i].configure(fg_color='transparent')


    def button_callback(self, index):
        self._current_index = index
        self.change_images_color()