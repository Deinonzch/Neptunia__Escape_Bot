from Class.EscapeBotMenu import *
from Class.BotMenu import *
import time


class ListOfBotsMenu(BotMenu):
    def __init__(self, surface, size):
        super().__init__(surface)
        self.__start_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Run")
        self.__back_button = Button(surface, [size[0] / 2, (size[1]) / 2], "Back")
        self.__escape_bot_menu = EscapeBotMenu(surface, size)

    def events(self):
        for event in pygame.event.get():
            self._clicked_run_button(event.type)
            self._clicked_back_button(event.type)
            self.clicked_exit_button_of_window(event.type)

    def _clicked_run_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__start_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._go_to_escape_bot_menu()
            self.__start_button.unclicked()

    def _clicked_back_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__back_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._back_to_main_menu()
            self.__back_button.unclicked()

    def draw(self):
        self._surface.fill((0, 0, 0))
        self.__start_button.draw()
        self.__back_button.draw()
        pygame.display.flip()

    def run(self):
        self._run_menu()

    def _back_to_main_menu(self):
        if self.__back_button.is_clicked():
            self._back()

    def _go_to_escape_bot_menu(self):
        self._initial_bot()
        self.__escape_bot_menu.draw()
        self._bot_menu_events()

    def _initial_bot(self):
        if self.__start_button.is_clicked():
            self.__escape_bot_menu.run()

    def _bot_menu_events(self):
        while self.__escape_bot_menu.is_done():
            self.__escape_bot_menu.events()

    def _back(self):
        if self.__back_button.is_clicked():
            self._exit_menu()
