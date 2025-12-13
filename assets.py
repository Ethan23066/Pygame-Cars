import pygame
import settings
import os

def load_png(filename, size=None):
    """
    Charge un fichier PNG depuis assets/sprites/.
    - filename : nom du fichier (ex: "car.png")
    - size : tuple (w, h) pour redimensionner, sinon SPRITE_SIZE par défaut
    """
    path = os.path.join(settings.ASSETS_DIR, filename)
    image = pygame.image.load(path).convert_alpha()

    if size:
        return pygame.transform.scale(image, size)
    return pygame.transform.scale(image, (settings.SPRITE_SIZE, settings.SPRITE_SIZE))

