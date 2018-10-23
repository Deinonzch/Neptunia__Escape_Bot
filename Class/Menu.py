import pygame
import sys


class Menu:
    def __init__(self, surface):
        self._surface = surface

    def clicked_exit_button_of_window(self, event_type):
        if event_type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
