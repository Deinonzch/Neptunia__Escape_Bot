import keyboard
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
            time.sleep(8.5)
            self.have_break()
            if not self.undone:
                break
            keyboard.press_and_release('r')
            self.have_break()
            if not self.undone:
                break
            time.sleep(0.5)
            keyboard.press_and_release('l')

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
