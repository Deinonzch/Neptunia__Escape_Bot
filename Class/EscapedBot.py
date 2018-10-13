from Class.ImageRecognition import is_first_menu_attack, is_second_menu_attack
from Class.Bot import *


class EscapedBot(Bot):
    def escape(self):
        while self._undone:
            self.__change_menu_if_is_first_attack_menu()
            self.__escape_if_is_second_attack_menu()
            self._have_break()

    def __change_menu_if_is_first_attack_menu(self):
        if is_first_menu_attack():
            self.__press_change_attack_menu_key()

    def __escape_if_is_second_attack_menu(self):
        if is_second_menu_attack():
            self.__press_escape_key()

    @staticmethod
    def __press_escape_key():
        keyboard.press_and_release('l')

    @staticmethod
    def __press_change_attack_menu_key():
        keyboard.press_and_release('r')
