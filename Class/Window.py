import pygame
import sys


def events(bot):
    for event in pygame.event.get():
        keyboard_events(event.type, bot)
        clicked_exit_button_of_window(event.type, bot)


def keyboard_events(event_type, bot):
    if event_type == pygame.KEYDOWN:
        exit_if_q(bot)


def exit_if_q(bot):
    if pygame.key.get_pressed()[pygame.K_q]:
        pygame.quit()
        bot.finish()
        sys.exit(0)


def clicked_exit_button_of_window(event_type, bot):
    if event_type == pygame.QUIT:
        pygame.quit()
        bot.finish()
        sys.exit(0)
