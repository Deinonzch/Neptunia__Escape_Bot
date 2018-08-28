from Class.Window import *
import threading
from Class.EscapedBot import *

pygame.init()

size = [500, 700]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

bot = EscapedBot()

t = threading.Thread(target=bot.escape, name='thread1')

t.start()

while True:
    events(bot)
