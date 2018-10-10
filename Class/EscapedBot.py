import keyboard
from Class.ImageRecognition import is_first_menu_attack, is_second_menu_attack


class EscapedBot:
    def __init__(self):
        self.__undone = True
        self.__break = False

    def listener(self):
        while self.__undone:
            self.if_end_key_is_pressed_work_is_done()
            self.if_stop_key_is_pressed_do_break()
            self.if_restart_key_is_pressed_back_to_work()

    def if_end_key_is_pressed_work_is_done(self):
        if keyboard.is_pressed('q'):
            self.finish()

    def finish(self):
        self.__undone = False

    def if_stop_key_is_pressed_do_break(self):
        if keyboard.is_pressed('alt+x'):
            self.stop()

    def stop(self):
        self.__break = True

    def if_restart_key_is_pressed_back_to_work(self):
        if keyboard.is_pressed('alt+z'):
            self.restart()

    def restart(self):
        self.__break = False

    def escape(self):
        while self.__undone:
            self.change_menu_if_is_first_attack_menu()
            self.excape_if_is_second_attack_menu()
            self.have_break()

    @staticmethod
    def change_menu_if_is_first_attack_menu():
        if is_first_menu_attack():
            change_attack_menu()

    @staticmethod
    def excape_if_is_second_attack_menu():
        if is_second_menu_attack():
            escape()

    def have_break(self):
        while self.__break and self.__undone:
            print('I have a break')


def escape():
    keyboard.press_and_release('l')


def change_attack_menu():
    keyboard.press_and_release('r')
