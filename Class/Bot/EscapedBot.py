from Class.OCR.ImageRecognition import is_first_menu_attack, is_second_menu_attack, is_run_screen, i_am_in_a_inventory
from Class.Bot.Bot import *
import time


class EscapedBot(Bot):
    def escape(self):
        while self._undone:
            self.__change_menu_if_is_first_attack_menu()
            self.__i_am_in_the_inventory()
            self.__escape_if_is_second_attack_menu()
            self._have_break()

    def __change_menu_if_is_first_attack_menu(self):
        if is_first_menu_attack():
            self.__run_change_menu_moves()
            time.sleep(0.05)
            self.__run_escape_moves()

    def __i_am_in_the_inventory(self):
        if i_am_in_a_inventory():
            self.__exit_from_the_inventory()
            time.sleep(0.05)


    def __escape_if_is_second_attack_menu(self):
        if is_second_menu_attack():
            self.__run_escape_moves()

    def __run_change_menu_moves(self):
        if not self._break or self._undone:
            self.__press_change_attack_menu_key()

    def __run_escape_moves(self):
        if not self._break or self._undone:
            self.__press_escape_key()
            self.__is_run_screen()

    def __exit_from_the_inventory(self):
        if not self._break or self._undone:
            self.__press_escape_key()

    def __is_run_screen(self):
        for each in range(0, 8):
            self.__attack_if_was_run_screen()

    def __attack_if_was_run_screen(self):
        if is_run_screen():
            self.__multiple_press_attack_key()

    def __multiple_press_attack_key(self):
        time.sleep(1.0)
        for i in range(0, 80):
            if self._break or not self._undone:
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
