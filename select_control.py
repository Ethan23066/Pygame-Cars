import pygame
from control_keyboard import KeyboardController
from control_gamepad import GamepadController

def select_controller():
    pygame.joystick.init()
    # Si une manette est détectée (USB ou Bluetooth), on la prend
    if pygame.joystick.get_count() > 0:
        return GamepadController()
    # Sinon, on reste sur le clavier
    return KeyboardController()
