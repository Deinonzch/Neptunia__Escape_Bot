from unittest import TestCase
from Class import EscapedBot

class TestEscapedBot(TestCase):
    def test_init(self):
        bot = EscapedBot.EscapedBot()
        self.assertEqual(bot.undone, True, 'undone is not True')
        self.assertEqual(bot.stop, False, 'stop is not False')

    def test_finished(self):
        bot = EscapedBot.EscapedBot()
        bot.finished()
        self.assertEqual(bot.undone, False, 'undone is not false')

    def test_stoped(self):
        bot = EscapedBot.EscapedBot()
        bot.stoped()
        self.assertEqual(bot.stop, True, 'stop is not True')

    def test_restarted(self):
        bot = EscapedBot.EscapedBot()
        bot.stoped()
        self.assertEqual(bot.stop, True, 'stop is not True')
        bot.restarted()
        self.assertEqual(bot.stop, False, 'stop is not False')
