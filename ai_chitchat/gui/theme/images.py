from enum import Enum

ICON_PATH = 'assets/icons/'
class BrandImagePath:
    TOP_BUTTON = ICON_PATH + 'house.png'
    CHAT_BUTTON = ICON_PATH + 'chat-dots.png'
    CANCEL_BUTTON = ICON_PATH + 'x-circle.png'
    MUTE_ON_BUTTON = ICON_PATH + 'volume-mute-fill.png'
    MUTE_OFF_BUTTON = ICON_PATH + 'volume-up-fill.png'
    REPLAY_BUTTON = ICON_PATH + 'arrow-counterclockwise.png'
    DOWNLOAD_BUTTON = ICON_PATH + 'download.png'

GALLERY_PATH = 'assets/images/'
class GalleryImagePath(Enum):
    img1 = GALLERY_PATH + 'monster01.png'
    img2 = GALLERY_PATH + 'monster02.png'
    img3 = GALLERY_PATH + 'monster03.png'
    img4 = GALLERY_PATH + 'monster04.png'
    img5 = GALLERY_PATH + 'monster05.png'
    img6 = GALLERY_PATH + 'monster06.png'

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]