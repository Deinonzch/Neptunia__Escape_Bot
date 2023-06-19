from unittest import TestCase
from Class.OCR.ImageRecognition import is_exedrive


class TestIsExedrive(TestCase):
    def test_is_exedrive_true_for_regex_EXEDrive(self):
        score = is_exedrive('EXEDrive')
        self.assertEqual(score, True)

    def test_is_exedrive_false_for_regex_FXFDrive(self):
        score = is_exedrive('FXFDrive')
        self.assertEqual(score, False)

    def test_is_exedrive_false_for_regex_mskovmpxjR8v(self):
        score = is_exedrive('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_exedrive_true_for_regex_EXEDriveEXEDrive(self):
        score = is_exedrive('EXEDriveEXEDrive')
        self.assertEqual(score, True)

    def test_is_exedrive_true_for_regex_afaEXEDrivesvs(self):
        score = is_exedrive('afaEXEDrivesvs')
        self.assertEqual(score, True)

    def test_is_exedrive_true_for_regex_EXEDrivefvsdbfd(self):
        score = is_exedrive('EXEDrivefvsdbfd')
        self.assertEqual(score, True)

    def test_is_exedrive_true_for_regex_sdbsbEXEDrive(self):
        score = is_exedrive('sdbsbEXEDrive')
        self.assertEqual(score, True)
