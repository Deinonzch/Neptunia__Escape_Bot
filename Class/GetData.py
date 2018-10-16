import logging
import datetime
from pathlib import Path


def save_data(text):
    date = datetime.datetime.now()
    data_folder = Path(r"C:/Users/Deinonzch/Documents/GitHub/Neptunia__Escape_Bot/Class/Data/ImageRecognition/")
    name = 'menu_text_OCR_' + str(date.day) + '-' + str(date.month) + '-' + str(date.year) + '.txt'
    file_to_open = data_folder / name
    try:
        file = open(file_to_open, 'a')
        print(text)
        file.write(text + '\n')
        file.close()
    except Exception as e:
        logging.exception(e)


def save_data_if_any_empty(text):
    if text != '':
        save_data(text)
