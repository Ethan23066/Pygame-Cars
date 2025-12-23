# select_sprite.py
import os
import pygame

class SelectSprite:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        self.base_dir = "assets"
        self.sprites = []

        for root, _, files in os.walk(self.base_dir):
            for f in files:
                if f.lower().endswith(".png"):
                    # chemin relatif depuis assets/
                    path = os.path.relpath(
                        os.path.join(root, f),
                        self.base_dir
                    )
                    self.sprites.append(path)

        if not self.sprites:
            raise RuntimeError("Aucun sprite trouvé dans assets/")

        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.sprites)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.sprites)
            elif event.key == pygame.K_RETURN:
                return self.sprites[self.selected]  # ex: "kart/Kart_R2D2KT.png"
        return None

    def draw(self):
        self.screen.fill((20, 20, 20))
        for i, name in enumerate(self.sprites):
            label = name.replace("\\", "/")  # affichage propre
            color = (255, 255, 255) if i == self.selected else (150, 150, 150)
            surf = self.font.render(label, True, color)
            self.screen.blit(surf, (80, 140 + i * 36))
