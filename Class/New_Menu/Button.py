import pygame


class Button:
    __length = 100
    __width = 15
    __color_of_unclicked = (150, 150, 150)
    __color_of_clicked = (10, 150, 10)
    __color_of_text = (0, 0, 0)
    __clicked = False

    def __init__(self, surface, start_point, text):
        self.__surface = surface
        self.__start_point = [start_point[0] - self.__length/2, start_point[1] - self.__width/2]
        self.text = text

    def draw(self):
        if self.__clicked:
            pygame.draw.rect(self.__surface, self.__color_of_clicked,
                             (self.__start_point[0], self.__start_point[1], self.__length, self.__width))
            self.text_print()
        else:
            pygame.draw.rect(self.__surface, self.__color_of_unclicked,
                             (self.__start_point[0], self.__start_point[1], self.__length, self.__width))
            self.text_print()

    def text_print(self):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 12)
        text = font.render(self.text, True, self.__color_of_text)
        self.__surface.blit(text, (self.__start_point[0] + self.__length/2 - text.get_rect()[2]/2,
                                   self.__start_point[1] + self.__width/2 - text.get_rect()[3]/2))
        pygame.font.quit()

    def clicked(self):
        position = pygame.mouse.get_pos()
        if self.__start_point[0] < position[0] < self.__start_point[0] + self.__length \
                and self.__start_point[1] < position[1] < self.__start_point[1] + self.__width:
            self.__clicked = True

    def unclicked(self):
        self.__clicked = False

    def is_clicked(self):
        if self.__clicked:
            return True
        else:
            return False
