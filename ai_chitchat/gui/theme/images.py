from enum import Enum

class BrandImagePath:
    TOP_BUTTON = 'assets/icons/house.png'
    CHAT_BUTTON = 'assets/icons/chat-dots.png'

PATH = 'assets/images/'
class GalleryImagePath(Enum):
    img1 = PATH + 'monster01.png'
    img2 = PATH + 'monster02.png'
    img3 = PATH + 'monster03.png'
    img4 = PATH + 'monster04.png'
    img5 = PATH + 'monster05.png'
    img6 = PATH + 'monster06.png'
    img7 = PATH + 'monster07.png'
    img8 = PATH + 'monster08.png'
    img9 = PATH + 'monster09.png'

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]