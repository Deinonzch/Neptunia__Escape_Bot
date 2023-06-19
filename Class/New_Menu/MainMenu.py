from Class.New_Menu.Menu import *
from Class.New_Menu.Button import *
import time


class MainMenu(Menu):
    def __init__(self, surface, size):
        super().__init__(surface)
        self.__start_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Run")
        self.__exit_button = Button(surface, [size[0] / 2, (size[1]) / 2], "Exit")

    def events(self):
        for event in pygame.event.get():
            self._clicked_exit_button(event.type)
            self.clicked_exit_button_of_window(event.type)
            self._clicked_run_button(event.type)

    def _clicked_run_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__start_button.clicked()
            self.draw()
            time.sleep(0.1)
            self.__start_button.unclicked()
            self.draw()

    def _clicked_exit_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__exit_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._exit()

    def draw(self):
        self._surface.fill((0, 0, 0))
        self.__start_button.draw()
        self.__exit_button.draw()
        pygame.display.flip()


    def _exit(self):
        if self.__exit_button.is_clicked():
            pygame.quit()
            sys.exit(0)
