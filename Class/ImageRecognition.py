try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import PIL.ImageGrab
import re


regex_1 = re.compile(r'.*(SPSkills)')
regex_2 = re.compile(r'.*(EXEDrive)')
regex_3 = re.compile(r'.*(([Aa])ttack)')
regex_4 = re.compile(r'.*(([Dd])efend)')
regex_5 = re.compile(r'.*(HDD0N)')
regex_6 = re.compile(r'.*(([Ss])witch)')
regex_7 = re.compile(r'.*(([Ii])tem)')
regex_8 = re.compile(r'.*(([Ee])scape)|(Esmane)')

regexes_1 = [regex_1, regex_2, regex_3, regex_4]
regexes_2 = [regex_5, regex_6, regex_7, regex_8]

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Deinonzch\AppData\Local\Tesseract-OCR\tesseract'

area1 = (1570, 650, 1750, 720)
area2 = (1540, 700, 1700, 760)
area3 = (1510, 750, 1650, 830)
#1480, 800, 1600, 880
#1470, 810, 1600, 880
attack_menu_button_4 = (1470, 810, 1600, 880)

areas = [area1, area2, area3, attack_menu_button_4]


def get_text(place):
    menu_attack = PIL.ImageGrab.grab().crop(place)
    return pytesseract.image_to_string(menu_attack).replace(' ', '')


def is_defend(text):
    if re.findall(regex_4, text):
        print(text)
        return True
    else:
        return False


def is_escape(text):
    print(text)
    if re.findall(regex_8, text):
        return True
    else:
        return False
