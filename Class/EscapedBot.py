from Class.ImageRecognition import is_first_menu_attack, is_second_menu_attack, is_run_screen
from Class.Bot import *
import time
import threading


class EscapedBot(Bot):
    def escape(self):
        while self._undone:
            self.__change_menu_if_is_first_attack_menu()
            self.__escape_if_is_second_attack_menu()
            self.__attack_if_was_run_screen()
            self._have_break()

    def __change_menu_if_is_first_attack_menu(self):
        if is_first_menu_attack():
            self.__press_change_attack_menu_key()

    def __escape_if_is_second_attack_menu(self):
        if is_second_menu_attack():
            self.__press_escape_key()

    def __attack_if_was_run_screen(self):
        if is_run_screen():
            bot_thred = threading.Thread(target=self.__attack(), name='threadbot1')
            bot_thred.start()

    def __attack(self):
        self.__multiple_press_attack_key()

    def __multiple_press_attack_key(self):
        time.sleep(1.8)
        for i in range(0, 150):
            if self._break:
                break
            self.__press_attack_key()

    @staticmethod
    def __press_escape_key():
        keyboard.press_and_release('l')

    @staticmethod
    def __press_change_attack_menu_key():
        keyboard.press_and_release('r')

    @staticmethod
    def __press_attack_key():
        keyboard.press_and_release('k')
