from unittest import TestCase
from Class.OCR.ImageRecognition import is_switch


class TestIsSwitch(TestCase):
    def test_is_switch_true_for_regex_Switch(self):
        score = is_switch('Switch')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_5witch(self):
        score = is_switch('5witch')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_switch(self):
        score = is_switch('switch')
        self.assertEqual(score, True)

    def test_is_switch_false_for_regex_Swifch(self):
        score = is_switch('Swifch')
        self.assertEqual(score, False)

    def test_is_switch_false_for_regex_swifch(self):
        score = is_switch('swifch')
        self.assertEqual(score, False)

    def test_is_switch_false_for_regex_mskovmpxjR8v(self):
        score = is_switch('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_switch_true_for_regex_SwitchSwitch(self):
        score = is_switch('SwitchSwitch')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_switchswitch(self):
        score = is_switch('switchswitch')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_afaSwitchvs(self):
        score = is_switch('afaSwitchvs')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_afaswitchvs(self):
        score = is_switch('afaswitchvs')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_Switchfvsdbfd(self):
        score = is_switch('Switchfvsdbfd')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_switchfvsdbfd(self):
        score = is_switch('switchfvsdbfd')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_sdbsbSwitch(self):
        score = is_switch('sdbsbSwitch')
        self.assertEqual(score, True)

    def test_is_switch_true_for_regex_sdbsbswitch(self):
        score = is_switch('sdbsbswitch')
        self.assertEqual(score, True)
