import unittest
from Class.OCR.ImageRecognition import regexes_attack_menu_1, regexes_attack_menu_2


class RegexImageRecognition(unittest.TestCase):
    def test_regex_SPSkills(self):
        self.assertRegex("SPSkills", regexes_attack_menu_1[0])

    def test_regex_SPSkills_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_1[0])

    def test_regex_EXEDrive(self):
        self.assertRegex("EXEDrive", regexes_attack_menu_1[1])

    def test_regex_EXEDrive_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_1[1])

    def test_regex_Attack(self):
        self.assertRegex("Attack", regexes_attack_menu_1[2])

    def test_regex_Attack_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_1[2])

    def test_regex_Defend(self):
        self.assertRegex("Defend", regexes_attack_menu_1[3])

    def test_regex_Defend_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_1[3])

    def test_regex_HDDON(self):
        self.assertRegex("HDDON", regexes_attack_menu_2[0])

    def test_regex_HDDON_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_2[0])

    def test_regex_Switch(self):
        self.assertRegex("Switch", regexes_attack_menu_2[1])

    def test_regex_Switch_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_2[1])

    def test_regex_Item(self):
        self.assertRegex("Item", regexes_attack_menu_2[2])

    def test_regex_Item_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_2[2])

    def test_regex_Escape(self):
        self.assertRegex("Escape", regexes_attack_menu_2[3])

    def test_regex_Escape_uncorrect_text(self):
        self.assertNotRegex("dfvkasvka", regexes_attack_menu_2[3])
