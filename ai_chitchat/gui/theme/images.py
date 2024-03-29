from enum import Enum

ICON_PATH = 'assets/icons/'
class BrandImagePath:
    TOP_BUTTON = ICON_PATH + 'house.png'
    CHAT_BUTTON = ICON_PATH + 'chat-dots.png'
    CANCEL_BUTTON = ICON_PATH + 'x-circle.png'
    SOUND_ICON = ICON_PATH + 'volume-up-fill.png'
    REPLAY_BUTTON = ICON_PATH + 'arrow-counterclockwise.png'
    DOWNLOAD_BUTTON = ICON_PATH + 'download.png'
    SUBMIT_BUTTON = ICON_PATH + 'arrow-up-circle-fill.png'
    USER_ICON = ICON_PATH + 'person-fill.png'

GALLERY_PATH = 'assets/images/'
class GalleryImagePath(Enum):
    img1 = GALLERY_PATH + 'sample01.png'
    img2 = GALLERY_PATH + 'sample02.png'
    img3 = GALLERY_PATH + 'sample03.png'
    img4 = GALLERY_PATH + 'sample04.png'
    img5 = GALLERY_PATH + 'sample05.png'
    img6 = GALLERY_PATH + 'sample06.png'

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]