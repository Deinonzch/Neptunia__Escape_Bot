from Class.EscapeBotMenu import *
import time
import sys


class MainMenu:
    def __init__(self, surface, size):
        self.__surface = surface
        self.__start_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Run")
        self.__exit_button = Button(surface, [size[0] / 2, (size[1]) / 2], "Exit")
        self.__escape_bot_menu = EscapeBotMenu(surface, size)

    def events(self):
        for event in pygame.event.get():
            self._clicked_run_button(event.type)
            self._clicked_exit_button(event.type)
            self.clicked_exit_button_of_window(event.type)

    def _clicked_run_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            print("a")
            self.__start_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._go_to_escape_bot_menu()
            self.__start_button.unclicked()

    def _clicked_exit_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__exit_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._exit()

    def draw(self):
        self.__surface.fill((0, 0, 0))
        self.__start_button.draw()
        self.__exit_button.draw()
        pygame.display.flip()

    def _go_to_escape_bot_menu(self):
        if self.__start_button.is_clicked():
            self.__escape_bot_menu.run()
        while self.__escape_bot_menu.is_done():
            self.__escape_bot_menu.draw()
            self.__escape_bot_menu.events()

    def _exit(self):
        if self.__exit_button.is_clicked():
            pygame.quit()
            sys.exit(0)

    @staticmethod
    def clicked_exit_button_of_window(event_type):
        if event_type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
