from unittest import TestCase
from Class.ImageRecognition import is_hddon_or_awakened


class TestIsHddon(TestCase):
    def test_is_hddon_for_regex_HDD0N(self):
        score = is_hddon_or_awakened('HDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_for_regex_HDDON(self):
        score = is_hddon_or_awakened('HDDON')
        self.assertEqual(score, True)

    def test_is_hddon_false_for_regex_HDD0M(self):
        score = is_hddon_or_awakened('HDD0M')
        self.assertEqual(score, False)

    def test_is_hddon_false_for_regex_HDDOM(self):
        score = is_hddon_or_awakened('HDDOM')
        self.assertEqual(score, False)

    def test_is_hddon_false_for_regex_mskovmpxjR8v(self):
        score = is_hddon_or_awakened('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_hddon_true_for_regex_HDD0NHDD0N(self):
        score = is_hddon_or_awakened('HDD0NHDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDDONHDDON(self):
        score = is_hddon_or_awakened('HDDONHDDON')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_afaHDD0Nvs(self):
        score = is_hddon_or_awakened('afaHDD0Nvs')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_afaHDDONvs(self):
        score = is_hddon_or_awakened('afaHDDONvs')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDD0Nfvsdbfd(self):
        score = is_hddon_or_awakened('HDD0Nfvsdbfd')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDDONfvsdbfd(self):
        score = is_hddon_or_awakened('HDDONfvsdbfd')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_sdbsbHDD0N(self):
        score = is_hddon_or_awakened('sdbsbHDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_sdbsbHDDON(self):
        score = is_hddon_or_awakened('sdbsbHDDON')
        self.assertEqual(score, True)

    def test_is_awakened_true_for_regex_Awakened(self):
        score = is_hddon_or_awakened('Awakened')
        self.assertEqual(score, True)

    def test_is_awakened_true_for_regex_Awakéned(self):
        score = is_hddon_or_awakened('Awakéned')
        self.assertEqual(score, True)

    def test_is_awakened_false_for_regex_Avakened(self):
        score = is_hddon_or_awakened('Avakened')
        self.assertEqual(score, False)

    def test_is_awakened_false_for_regex_mskovmpxjR8v(self):
        score = is_hddon_or_awakened('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_awakened_true_for_regex_AwakenedAwakened(self):
        score = is_hddon_or_awakened('AwakenedAwakened')
        self.assertEqual(score, True)

    def test_is_awakened_true_for_regex_afaAwakenedvs(self):
        score = is_hddon_or_awakened('afaAwakenedvs')
        self.assertEqual(score, True)

    def test_is_awakened_true_for_regex_Awakenedsfvsdbfd(self):
        score = is_hddon_or_awakened('Awakenedsfvsdbfd')
        self.assertEqual(score, True)

    def test_is_awakened_true_for_regex_sdbsbAwakened(self):
        score = is_hddon_or_awakened('sdbsbAwakened')
        self.assertEqual(score, True)

