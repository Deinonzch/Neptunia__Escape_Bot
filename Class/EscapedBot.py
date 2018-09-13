import keyboard
from Class.ImageRecognition import get_menu_attack_text, is_first_menu_attack, is_escape


class EscapedBot:
    def __init__(self):
        self.undone = True
        self.stop = False

    def listener(self):
        while self.undone:
            self.if_end_key_is_pressed_work_is_done()
            self.if_stop_key_is_pressed_do_break()
            self.if_restart_key_is_pressed_back_to_work()

    def if_end_key_is_pressed_work_is_done(self):
        if keyboard.is_pressed('q'):
            self.finished()

    def finished(self):
        self.undone = False

    def if_stop_key_is_pressed_do_break(self):
        if keyboard.is_pressed('alt+x'):
            self.stoped()

    def stoped(self):
        self.stop = True

    def if_restart_key_is_pressed_back_to_work(self):
        if keyboard.is_pressed('alt+z'):
            self.restarted()

    def restarted(self):
        self.stop = False

    def escape(self):
        while self.undone:
            texts = get_menu_attack_text()
            self.change_attack_menu_if_is_first(texts)
            self.if_attack_menu_have_escape_button_excape(texts[3])
            self.have_break()

    @staticmethod
    def change_attack_menu_if_is_first(texts):
        if is_first_menu_attack(texts):
            keyboard.press_and_release('r')

    @staticmethod
    def if_attack_menu_have_escape_button_excape(text):
        if is_escape(text):
            escape()

    def have_break(self):
        while self.stop and self.undone:
            print('I have a break')


def escape():
    keyboard.press_and_release('l')
