from unittest import TestCase
from Class.OCR.ImageRecognition import is_first_menu_attack


class TestIsFirstMenuAttack(TestCase):
    def test_is_first_menu_attack(self):
        score = is_first_menu_attack()
        self.assertEqual(score, False)
