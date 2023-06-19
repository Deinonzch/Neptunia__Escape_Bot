from unittest import TestCase
from Class.OCR.ImageRecognition import is_defend


class TestIsDefend(TestCase):
    def test_is_defend_true_for_regex_Defend(self):
        score = is_defend('Defend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_Defand(self):
        score = is_defend('Defand')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defend(self):
        score = is_defend('defend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defand(self):
        score = is_defend('defand')
        self.assertEqual(score, True)

    def test_is_defend_false_for_regex_Deferd(self):
        score = is_defend('Deferd')
        self.assertEqual(score, False)

    def test_is_defend_false_for_regex_Defard(self):
        score = is_defend('Defard')
        self.assertEqual(score, False)

    def test_is_defend_false_for_regex_deferd(self):
        score = is_defend('deferd')
        self.assertEqual(score, False)

    def test_is_defend_false_for_regex_defard(self):
        score = is_defend('defard')
        self.assertEqual(score, False)

    def test_is_defend_false_for_regex_mskovmpxjR8v(self):
        score = is_defend('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_defend_true_for_regex_DefendDefend(self):
        score = is_defend('DefendDefend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_DefandDefand(self):
        score = is_defend('DefandDefand')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defenddefend(self):
        score = is_defend('defenddefend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defanddefand(self):
        score = is_defend('defanddefand')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_afaDefendvs(self):
        score = is_defend('afaDefendvs')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_afaDefandvs(self):
        score = is_defend('afaDefandvs')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_afadefendvs(self):
        score = is_defend('afadefendvs')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_afadefandvs(self):
        score = is_defend('afadefandvs')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_Defendfvsdbfd(self):
        score = is_defend('Defendfvsdbfd')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_Defandfvsdbfd(self):
        score = is_defend('Defandfvsdbfd')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defendfvsdbfd(self):
        score = is_defend('defendfvsdbfd')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_defandfvsdbfd(self):
        score = is_defend('defandfvsdbfd')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_sdbsbDefend(self):
        score = is_defend('sdbsbDefend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_sdbsbDefand(self):
        score = is_defend('sdbsbDefand')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_sdbsbdefend(self):
        score = is_defend('sdbsbdefend')
        self.assertEqual(score, True)

    def test_is_defend_true_for_regex_sdbsbdefand(self):
        score = is_defend('sdbsbdefand')
        self.assertEqual(score, True)
