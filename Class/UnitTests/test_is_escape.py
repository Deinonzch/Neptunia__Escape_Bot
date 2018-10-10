from unittest import TestCase
from Class.ImageRecognition import is_escape


class TestIsEscape(TestCase):
    def test_is_escape_true_for_regex_Escape(self):
        score = is_escape('Escape')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_Esmane(self):
        score = is_escape('Esmane')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_escape(self):
        score = is_escape('escape')
        self.assertEqual(score, True)

    def test_is_escape_false_for_regex_Escepe(self):
        score = is_escape('Escepe')
        self.assertEqual(score, False)

    def test_is_escape_false_for_regex_escepe(self):
        score = is_escape('escepe')
        self.assertEqual(score, False)

    def test_is_escape_false_for_regex_mskovmpxjR8v(self):
        score = is_escape('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_escape_true_for_regex_EscapeEscape(self):
        score = is_escape('EscapeEscape')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_escapeescape(self):
        score = is_escape('escapeescape')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_afaEscapevs(self):
        score = is_escape('afaEscapevs')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_afaEsmanevs(self):
        score = is_escape('afaEsmanevs')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_afaescapevs(self):
        score = is_escape('afaescapevs')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_Escapefvsdbfd(self):
        score = is_escape('Escapefvsdbfd')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_Esmanefvsdbfd(self):
        score = is_escape('Esmanefvsdbfd')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_escapefvsdbfd(self):
        score = is_escape('escapefvsdbfd')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_sdbsbEscape(self):
        score = is_escape('sdbsbEscape')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_sdbsbEsmane(self):
        score = is_escape('sdbsbEsmane')
        self.assertEqual(score, True)

    def test_is_escape_true_for_regex_sdbsbescape(self):
        score = is_escape('sdbsbescape')
        self.assertEqual(score, True)
