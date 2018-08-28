import time
from Class.Window import *
from Class.KeyboardSimulation import *

pygame.init()

size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

pygame.init()

while True:
    time.sleep(8.5)
    PressKey(R)
    events()
    time.sleep(.5)
    ReleaseKey(R)
    events()
    time.sleep(.5)
    PressKey(L)
    events()
    time.sleep(.5)
    ReleaseKey(L)
    events()
