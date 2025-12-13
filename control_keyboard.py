import pygame

class KeyboardController:
    def get_input(self):
        k = pygame.key.get_pressed()
        return {"up":k[pygame.K_UP],"down":k[pygame.K_DOWN],
                "left":k[pygame.K_LEFT],"right":k[pygame.K_RIGHT]}
