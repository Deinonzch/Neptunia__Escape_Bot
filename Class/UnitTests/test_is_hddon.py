from unittest import TestCase
from Class.ImageRecognition import is_hddon


class TestIsHddon(TestCase):
    def test_is_hddon_for_regex_HDD0N(self):
        score = is_hddon('HDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_for_regex_HDDON(self):
        score = is_hddon('HDDON')
        self.assertEqual(score, True)

    def test_is_hddon_false_for_regex_HDD0M(self):
        score = is_hddon('HDD0M')
        self.assertEqual(score, False)

    def test_is_hddon_false_for_regex_HDDOM(self):
        score = is_hddon('HDDOM')
        self.assertEqual(score, False)

    def test_is_hddon_false_for_regex_mskovmpxjR8v(self):
        score = is_hddon('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_hddon_true_for_regex_HDD0NHDD0N(self):
        score = is_hddon('HDD0NHDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDDONHDDON(self):
        score = is_hddon('HDDONHDDON')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_afaHDD0Nvs(self):
        score = is_hddon('afaHDD0Nvs')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_afaHDDONvs(self):
        score = is_hddon('afaHDDONvs')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDD0Nfvsdbfd(self):
        score = is_hddon('HDD0Nfvsdbfd')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_HDDONfvsdbfd(self):
        score = is_hddon('HDDONfvsdbfd')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_sdbsbHDD0N(self):
        score = is_hddon('sdbsbHDD0N')
        self.assertEqual(score, True)

    def test_is_hddon_true_for_regex_sdbsbHDDON(self):
        score = is_hddon('sdbsbHDDON')
        self.assertEqual(score, True)

