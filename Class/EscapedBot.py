import keyboard
from Class.ImageRecognition import is_defend, is_escape, get_text, attack_menu_button_4
import time


class EscapedBot:
    def __init__(self):
        self.undone = True
        self.stop = False

    def finished(self):
        self.undone = False

    def stoped(self):
        self.stop = True

    def restarted(self):
        self.stop = False

    def listener(self):
        while self.undone:
            self.press_end_key()
            self.press_stop_key()
            self.press_restart_key()

    def escape(self):
        while self.undone:
            text = get_text(attack_menu_button_4)
            if is_defend(text):
                keyboard.press_and_release('r')
            time.sleep(0.5)
            if is_escape(text):
                keyboard.press_and_release('l')
            self.have_break()

    def press_end_key(self):
        if keyboard.is_pressed('q'):
            self.finished()

    def press_stop_key(self):
        if keyboard.is_pressed('alt+x'):
            self.stoped()

    def press_restart_key(self):
        if keyboard.is_pressed('alt+z'):
            self.restarted()

    def have_break(self):
        while self.stop and self.undone:
            print('I have a break')
