from unittest import TestCase
from Class.ImageRecognition import is_attack


class TestIsAttack(TestCase):
    def test_is_attack_true_for_regex_Attack(self):
        score = is_attack('Attack')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_attack(self):
        score = is_attack('attack')
        self.assertEqual(score, True)

    def test_is_attack_false_for_regex_Attaok(self):
        score = is_attack('Attaok')
        self.assertEqual(score, False)

    def test_is_attack_false_for_regex_attaok(self):
        score = is_attack('attaok')
        self.assertEqual(score, False)

    def test_is_attack_false_for_regex_mskovmpxjR8v(self):
        score = is_attack('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_attack_true_for_regex_AttackAttack(self):
        score = is_attack('AttackAttack')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_attackattack(self):
        score = is_attack('attackattack')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_afaAttackvs(self):
        score = is_attack('afaAttackvs')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_afaattackvs(self):
        score = is_attack('afaattackvs')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_Attackfvsdbfd(self):
        score = is_attack('Attackfvsdbfd')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_attackfvsdbfd(self):
        score = is_attack('attackfvsdbfd')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_sdbsbAttack(self):
        score = is_attack('sdbsbAttack')
        self.assertEqual(score, True)

    def test_is_attack_true_for_regex_sdbsbattack(self):
        score = is_attack('sdbsbattack')
        self.assertEqual(score, True)
