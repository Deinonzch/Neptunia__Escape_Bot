from Class.Menu.Button import *
from Class.Bot.EscapedBot import *
import threading
import time
from Class.Menu.BasicMenu import *


class EscapeBotMenu(BasicMenu):
    __bot = EscapedBot()

    def __init__(self, surface, size):
        super().__init__(surface)
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

    def clicked_exit_button_of_window(self, event_type):
        if event_type == pygame.QUIT:
            pygame.quit()
            self.__bot.finish()
            sys.exit(0)

    def draw(self):
        self._surface.fill((0, 0, 0))
        self.__exit_button.draw()
        pygame.display.flip()

    def _exit_escape_bot_menu(self):
        if self.__exit_button.is_clicked():
            self.exit()

    def run(self):
        self._run_menu()
        self._run_bot()

    def _run_bot(self):
        self.__bot.run()
        t = threading.Thread(target=self.__bot.escape, name='thread1')
        s = threading.Thread(target=self.__bot.listener, name='thread2')
        t.start()
        s.start()

    def exit(self):
        self._exit_menu()
        self._go_off_bot()

    def _go_off_bot(self):
        self.__bot.finish()
