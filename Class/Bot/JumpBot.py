from Class.Bot.Bot import *
import time


class JumpBot(Bot):
    def jump(self):
        while self._undone:
            self.__run_jump_moves()
            time.sleep(0.05)
            self._have_break()

    def __run_jump_moves(self):
        if not self._break or self._undone:
            self.__press_jump_key()

    @staticmethod
    def __press_jump_key():
        keyboard.press_and_release('l')
