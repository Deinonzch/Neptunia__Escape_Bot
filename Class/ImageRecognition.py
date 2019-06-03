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
regex_attack = re.compile(r'.*([Aa]ttack)')
regex_defend = re.compile(r'.*([Dd]ef[ae]nd)')
regex_hddon_or_awakened = re.compile(r'.*(HDD[0O]N)|(Awak[eé]ned)')
regex_switch = re.compile(r'.*([Ss5]witch)')
regex_item = re.compile(r'.*([Ii]te(m)|(rn))')
regex_escape = re.compile(r'.*([Ee]s[co]ape)|(Esmane)')
regex_run_text = re.compile(r'(R[au]n)')
regex_have = re.compile(r'([Hh]ave)')

regexes_attack_menu_1 = [regex_spskills, regex_exedrive, regex_attack, regex_defend]
regexes_attack_menu_2 = [regex_hddon_or_awakened, regex_switch, regex_item, regex_escape]

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Deinonzch\AppData\Local\Tesseract-OCR\tesseract'

attack_menu_button_1 = (1570, 650, 1750, 720)
attack_menu_button_2 = (1540, 700, 1700, 760)
attack_menu_button_3 = (1510, 750, 1650, 830)
attack_menu_button_4 = (1470, 810, 1590, 880)

place_of_have_text = (1185, 150, 1270, 200)

place_of_run_text = (775, 25, 1125, 75)

attack_menu_button_places = [attack_menu_button_1, attack_menu_button_2, attack_menu_button_3, attack_menu_button_4]


def is_first_menu_attack():
    text = get_texts_from_button_defend_or_escape()
    if is_defend(text):
        return True
    else:
        return False


def is_second_menu_attack():
    text = get_texts_from_button_defend_or_escape()
    if is_escape(text):
        return True
    else:
        return False


def i_am_in_a_inventory():
    text = get_texts_from_inventory()
    if is_have(text):
        return True
    else:
        return False


def is_run_screen():
    text = get_texts_from_upper_information_text()
    if is_run_text(text):
        return True
    else:
        return False


def is_failed_screen():
    text = get_texts_from_upper_information_text()
    if is_escape(text):
        return True
    else:
        return False


def get_texts_from_button_defend_or_escape():
    text = ''
    try:
        image = PIL.ImageGrab.grab(attack_menu_button_4)
        text = get_button_text_from(image)
    except Exception as e:
        logging.exception(e)
    return text


def get_texts_from_upper_information_text():
    text = ''
    try:
        image = PIL.ImageGrab.grab(place_of_run_text)
        text = get_button_text_from(image)
    except Exception as e:
        logging.exception(e)
    return text


def get_texts_from_inventory():
    text = ''
    try:
        image = PIL.ImageGrab.grab(place_of_have_text)
        text = get_button_text_from(image)
    except Exception as e:
        logging.exception(e)
    return text


def get_button_text_from(image):
    return pytesseract.image_to_string(image).replace(' ', '')


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


def is_hddon_or_awakened(text):
    if re.findall(regex_hddon_or_awakened, text):
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


def is_have(text):
    if re.findall(regex_have, text):
        return True
    else:
        return False


def is_run_text(text):
    if re.findall(regex_run_text, text):
        return True
    else:
        return False
