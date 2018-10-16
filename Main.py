from Class.MainMenu import *

pygame.init()

size = [500, 700]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

pygame.display.flip()

main_menu = MainMenu(screen, size)

while True:
    main_menu.draw()
    main_menu.events()
