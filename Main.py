import time
import pygame
import ctypes
import sys

SendInput = ctypes.windll.user32.SendInput

L = 0x26
R = 0x13

pygame.init()

size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def events():
    for event in pygame.event.get():
        keyboard_events(event.type)
        clicked_exit_button_of_window(event.type)


def keyboard_events(event_type):
    if event_type == pygame.KEYDOWN:
        exit_if_q()


def exit_if_q():
    if pygame.key.get_pressed()[pygame.K_q]:
        pygame.quit()
        sys.exit(0)


def clicked_exit_button_of_window(event_type):
    if event_type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)


def ecsape_moves():
    while True:
        time.sleep(8)
        PressKey(R)
        time.sleep(.5)
        ReleaseKey(R)
        time.sleep(.5)
        PressKey(L)
        time.sleep(.5)
        ReleaseKey(L)


def events_control():
    while True:
        events()

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)

pygame.init()

while True:
    time.sleep(8)
    PressKey(R)
    events()
    time.sleep(.5)
    ReleaseKey(R)
    events()
    time.sleep(.5)
    PressKey(L)
    events()
    time.sleep(.5)
    ReleaseKey(L)
    events()
