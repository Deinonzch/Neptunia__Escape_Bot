from unittest import TestCase
try:
    import Image
except ImportError:
    from PIL import Image
from pathlib import Path
from Class.ImageRecognition import get_button_text_from, attack_menu_button_4

# ')SPSkills', '\EXEDrive', 'Attack', ')Defend'
# ')HDD0N', 'Switch', 'Item', ')Esoape'


class TestGetButtonTextFrom(TestCase):
    def test_get_button_4_text_from_image__of_game_1(self):
        file_to_open = \
            Path(r"C:/Users/Deinonzch/Documents/GitHub/Neptunia__Escape_Bot/Class/Data/Image/image_of_game.jpg")
        img = Image.open(file_to_open)
        text = get_button_text_from(img.crop(attack_menu_button_4))
        self.assertEqual(text, ')Defend')

    def test_get_button_4_text_from_image__of_game_2(self):
        file_to_open = \
            Path(r"C:/Users/Deinonzch/Documents/GitHub/Neptunia__Escape_Bot/Class/Data/Image/image_of_game_2.jpg")
        img = Image.open(file_to_open)
        text = get_button_text_from(img.crop(attack_menu_button_4))
        self.assertEqual(text, ')Esoape')

    def test_get_button_4_text_from_image_of_pulpit(self):
        file_to_open = \
            Path(r"C:/Users/Deinonzch/Documents/GitHub/Neptunia__Escape_Bot/Class/Data/Image/image_of_pulpit.jpg")
        img = Image.open(file_to_open)
        text = get_button_text_from(img.crop(attack_menu_button_4))
        self.assertNotEqual(text, ')Defend')