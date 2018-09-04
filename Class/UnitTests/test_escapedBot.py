from unittest import TestCase
from Class import EscapedBot


class TestEscapedBot(TestCase):
    def test_init(self):
        bot = EscapedBot.EscapedBot()
        self.assertEqual(bot.undone, True)

    def test_finish(self):
        bot = EscapedBot.EscapedBot()
        bot.finish()
        self.assertEqual(bot.undone, False)
