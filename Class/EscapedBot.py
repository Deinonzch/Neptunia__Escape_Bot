from Class.KeyboardSimulation import *
import time


class EscapedBot:
    def __init__(self):
        self.undone = True

    def finish(self):
        self.undone = False

    def escape(self):
        while self.undone:
            time.sleep(8.5)
            PressKey(R)
            time.sleep(.5)
            ReleaseKey(R)
            time.sleep(.5)
            PressKey(L)
            time.sleep(.5)
            ReleaseKey(L)
