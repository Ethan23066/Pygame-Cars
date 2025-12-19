import os
import pygame

def load_png(relative_path):
    path = os.path.join("assets", relative_path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Sprite introuvable: {path}")
    return pygame.image.load(path).convert_alpha()
