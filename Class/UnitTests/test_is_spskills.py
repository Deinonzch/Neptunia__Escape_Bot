from unittest import TestCase
from Class.ImageRecognition import is_spskills


class TestIsSpskills(TestCase):
    def test_is_spskills_true_for_regex_SPSkills(self):
        score = is_spskills('SPSkills')
        self.assertEqual(score, True)

    def test_is_spskills_false_for_regex_2P2kills(self):
        score = is_spskills('2P2kills')
        self.assertEqual(score, False)

    def test_is_spskills_false_for_regex_mskovmpxjR8v(self):
        score = is_spskills('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_spskills_true_for_regex_SPSkillsSPSkills(self):
        score = is_spskills('SPSkillsSPSkills')
        self.assertEqual(score, True)

    def test_is_spskills_true_for_regex_afaSPSkillssvs(self):
        score = is_spskills('afaSPSkillssvs')
        self.assertEqual(score, True)

    def test_is_spskills_true_for_regex_SPSkillssfvsdbfd(self):
        score = is_spskills('SPSkillssfvsdbfd')
        self.assertEqual(score, True)

    def test_is_spskills_true_for_regex_sdbsbSPSkills(self):
        score = is_spskills('sdbsbSPSkills')
        self.assertEqual(score, True)
