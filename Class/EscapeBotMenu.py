from Class.Button import *
from Class.EscapedBot import *
import threading
import time
import sys


class EscapeBotMenu:
    __done = False
    __bot = EscapedBot()

    def __init__(self, surface, size):
        self.__surface = surface
        self.__exit_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Exit")

    def events(self):
        for event in pygame.event.get():
            self._clicked_exit_button(event.type)
            self.clicked_exit_button_of_window(event.type)

    def _clicked_exit_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__exit_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._exit_escape_bot_menu()
            self.__exit_button.unclicked()

    def draw(self):
        self.__surface.fill((0, 0, 0))
        self.__exit_button.draw()
        pygame.display.flip()

    def _exit_escape_bot_menu(self):
        if self.__exit_button.is_clicked():
            self.exit()

    def run(self):
        self._run_menu()
        self._run_bot()

    def _run_bot(self):
        t = threading.Thread(target=self.__bot.escape, name='thread1')
        s = threading.Thread(target=self.__bot.listener, name='thread2')
        t.start()
        s.start()

    def _run_menu(self):
        self.__done = True

    def exit(self):
        self._exit_menu()
        self._go_off_bot()

    def _go_off_bot(self):
        self.__bot.finish()

    def _exit_menu(self):
        self.__done = False

    def is_done(self):
        if self.__done:
            return True
        else:
            return False

    def clicked_exit_button_of_window(self, event_type):
        if event_type == pygame.QUIT:
            pygame.quit()
            self.__bot.finish()
            sys.exit(0)
