from Class.Bot.Bot import *
import time


class RunningBot(Bot):
    def running(self):
        back = False
        time_to_change_direction = time.time() + 2.5
        while self._undone:
            if not back:
                self.__run_running_moves()
            else:
                self.__run_running_back_moves()
            if time_to_change_direction < time.time():
                back = not back
                if back:
                    time_to_change_direction = time.time() + 2.5
                else:
                    time_to_change_direction = time.time() + 2.2
            self._have_break()

    def __run_running_moves(self):
        if not self._break or self._undone:
            self.__release_running_back_key()
            self.__press_running_key()

    def __run_running_back_moves(self):
        if not self._break or self._undone:
            self.__release_running_key()
            self.__press_running_back_key()

    @staticmethod
    def __press_running_key():
        keyboard.press('w')

    @staticmethod
    def __release_running_key():
        keyboard.release('w')

    @staticmethod
    def __press_running_back_key():
        keyboard.press('s')

    @staticmethod
    def __release_running_back_key():
        keyboard.release('s')
