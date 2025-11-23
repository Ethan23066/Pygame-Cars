# controls_keyboard.py
import pygame
import settings

class KeyboardController:
    def __init__(self):
        pass

    def update(self, player_rect):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= settings.PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_rect.x += settings.PLAYER_SPEED
        if keys[pygame.K_UP]:
            player_rect.y -= settings.PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player_rect.y += settings.PLAYER_SPEED
        return player_rect
