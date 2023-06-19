from Class.Menu.EscapeBotMenu import *
from Class.Menu.JumpBotMenu import *
from Class.Menu.RunningBotMenu import *
from Class.Menu.BasicMenu import *
import time


class ListOfBotsMenu(BasicMenu):
    def __init__(self, surface, size):
        super().__init__(surface)
        self.__start_escape_button = Button(surface, [size[0] / 2, (size[1] - 300) / 2], "Run Escape Bot")
        self.__start_jump_button = Button(surface, [size[0] / 2, (size[1] - 200) / 2], "Run Jump Bot")
        self.__start_running_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Run Running Bot")
        self.__back_button = Button(surface, [size[0] / 2, (size[1]) / 2], "Back")
        self.__escape_bot_menu = EscapeBotMenu(surface, size)
        self.__jump_bot_menu = JumpBotMenu(surface, size)
        self.__running_bot_menu = RunningBotMenu(surface, size)

    def events(self):
        for event in pygame.event.get():
            self._clicked_run_escape_bot_button(event.type)
            self._clicked_run_jump_bot_button(event.type)
            self._clicked_run_running_bot_button(event.type)
            self._clicked_back_button(event.type)
            self.clicked_exit_button_of_window(event.type)

    def _clicked_run_escape_bot_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__start_escape_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._go_to_escape_bot_menu()
            self.__start_escape_button.unclicked()

    def _clicked_run_jump_bot_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__start_jump_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._go_to_jump_bot_menu()
            self.__start_jump_button.unclicked()

    def _clicked_run_running_bot_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__start_running_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._go_to_running_bot_menu()
            self.__start_running_button.unclicked()

    def _clicked_back_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__back_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._back_to_main_menu()
            self.__back_button.unclicked()

    def draw(self):
        self._surface.fill((0, 0, 0))
        self.__start_escape_button.draw()
        self.__start_jump_button.draw()
        self.__start_running_button.draw()
        self.__back_button.draw()
        pygame.display.flip()

    def run(self):
        self._run_menu()

    def _back_to_main_menu(self):
        if self.__back_button.is_clicked():
            self._back()

    def _go_to_escape_bot_menu(self):
        self._initial_escape_bot()
        self.__escape_bot_menu.draw()
        self._escape_bot_menu_events()

    def _go_to_jump_bot_menu(self):
        self._initial_jump_bot()
        self.__jump_bot_menu.draw()
        self._jump_bot_menu_events()

    def _go_to_running_bot_menu(self):
        self._initial_running_bot()
        self.__running_bot_menu.draw()
        self._running_bot_menu_events()

    def _initial_escape_bot(self):
        if self.__start_escape_button.is_clicked():
            self.__escape_bot_menu.run()

    def _initial_jump_bot(self):
        if self.__start_jump_button.is_clicked():
            self.__jump_bot_menu.run()

    def _initial_running_bot(self):
        if self.__start_running_button.is_clicked():
            self.__running_bot_menu.run()

    def _escape_bot_menu_events(self):
        while self.__escape_bot_menu.is_done():
            self.__escape_bot_menu.events()

    def _jump_bot_menu_events(self):
        while self.__jump_bot_menu.is_done():
            self.__jump_bot_menu.events()

    def _running_bot_menu_events(self):
        while self.__running_bot_menu.is_done():
            self.__running_bot_menu.events()

    def _back(self):
        if self.__back_button.is_clicked():
            self._exit_menu()
