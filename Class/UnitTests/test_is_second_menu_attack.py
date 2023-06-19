from unittest import TestCase
from Class.OCR.ImageRecognition import is_second_menu_attack


class TestIaSecondMenuAttack(TestCase):
    def test_is_second_menu_attack(self):
        score = is_second_menu_attack()
        self.assertEqual(score, False)
