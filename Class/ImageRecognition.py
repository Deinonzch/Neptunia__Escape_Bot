try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import PIL.ImageGrab
import re
import logging


regex_spskills = re.compile(r'.*(SPSkills)')
regex_exedrive = re.compile(r'.*(EXEDrive)')
regex_attack = re.compile(r'.*(([Aa])ttack)')
regex_defend = re.compile(r'.*(([Dd])ef[ae]nd)')
regex_hddon = re.compile(r'.*(HDD[0O]N)')
regex_switch = re.compile(r'.*(([Ss])witch)')
regex_item = re.compile(r'.*(([Ii])tem)')
regex_escape = re.compile(r'.*(([Ee])scape)|(Esmane)')

regexes_attack_menu_1 = [regex_spskills, regex_exedrive, regex_attack, regex_defend]
regexes_attack_menu_2 = [regex_hddon, regex_switch, regex_item, regex_escape]

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Deinonzch\AppData\Local\Tesseract-OCR\tesseract'

attack_menu_button_1 = (1570, 650, 1750, 720)
attack_menu_button_2 = (1540, 700, 1700, 760)
attack_menu_button_3 = (1510, 750, 1650, 830)
attack_menu_button_4 = (1470, 810, 1600, 880)

attack_menu_button_places = [attack_menu_button_1, attack_menu_button_2, attack_menu_button_3, attack_menu_button_4]


def is_first_menu_attack():
    texts = get_texts_from_menu_attack()
    if is_spskills(texts[0]) or is_exedrive(texts[1]) or is_attack(texts[2]) or is_defend(texts[3]):
        return True
    else:
        return False


def is_second_menu_attack():
    texts = get_texts_from_menu_attack()
    if is_hddon(texts[0]) or is_switch(texts[1]) or is_item(texts[2]) or is_escape(texts[3]):
        return True
    else:
        return False


def get_texts_from_menu_attack():
    image = get_image()
    texts = get_buttons_text_from(image)
    return texts


def get_image():
    try:
        image = PIL.ImageGrab.grab()
    except Exception as e:
        logging.exception(e)
    return image


def get_buttons_text_from(image):
    texts = []
    for button_place in attack_menu_button_places:
        button = get_button_from(image, button_place)
        text = pytesseract.image_to_string(button).replace(' ', '')
        texts.append(text)
    return texts


def get_button_from(image, place):
    image_button = image.crop(place)
    return image_button


def is_spskills(text):
    if re.findall(regex_spskills, text):
        return True
    else:
        return False


def is_exedrive(text):
    if re.findall(regex_exedrive, text):
        return True
    else:
        return False


def is_attack(text):
    if re.findall(regex_attack, text):
        return True
    else:
        return False


def is_defend(text):
    if re.findall(regex_defend, text):
        return True
    else:
        return False


def is_hddon(text):
    if re.findall(regex_hddon, text):
        return True
    else:
        return False


def is_switch(text):
    if re.findall(regex_switch, text):
        return True
    else:
        return False


def is_item(text):
    if re.findall(regex_item, text):
        return True
    else:
        return False


def is_escape(text):
    if re.findall(regex_escape, text):
        return True
    else:
        return False
