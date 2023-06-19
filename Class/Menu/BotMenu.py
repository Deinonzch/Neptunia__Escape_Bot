from Class.Menu.BasicMenu import *
from Class.Menu.Button import *
import time


class BotMenu(BasicMenu):

    def __init__(self, surface, size):
        super().__init__(surface)
        self.__exit_button = Button(surface, [size[0] / 2, (size[1] - 100) / 2], "Exit")

    def events(self):
        for event in pygame.event.get():
            self._clicked_exit_button(event.type)
            self.clicked_exit_button_of_window(event.type)

    def draw(self):
        self._surface.fill((0, 0, 0))
        self.__exit_button.draw()
        pygame.display.flip()

    def _clicked_exit_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.__exit_button.clicked()
            self.draw()
            time.sleep(0.1)
            self.__exit_button.unclicked()
