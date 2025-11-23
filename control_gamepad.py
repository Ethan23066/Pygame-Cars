# controls_gamepad.py
import pygame
import settings

class GamepadController:
    def __init__(self):
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        else:
            self.joystick = None

    def update(self, player_rect):
        if not self.joystick:
            return player_rect

        # Axe gauche/droite
        axis_x = self.joystick.get_axis(0)
        # Axe haut/bas
        axis_y = self.joystick.get_axis(1)

        player_rect.x += int(axis_x * settings.PLAYER_SPEED)
        player_rect.y += int(axis_y * settings.PLAYER_SPEED)

        return player_rect
