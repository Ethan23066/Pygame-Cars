import pygame
import os

class SelectMap:
    def __init__(self, screen, maps_dir="maps"):
        self.screen = screen
        self.maps = [f for f in os.listdir(maps_dir) if f.endswith(".tmx")]
        self.selected = 0
        self.font = pygame.font.Font(None, 36)
        self.w, self.h = screen.get_size()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.maps)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.maps)
            elif event.key == pygame.K_RETURN:
                return self.maps[self.selected]
            elif event.key == pygame.K_ESCAPE:
                return "BACK"
        return None

    def draw(self):
        self.screen.fill((10, 10, 10))
        title = self.font.render("Choisir une carte", True, (200, 200, 200))
        self.screen.blit(title, title.get_rect(center=(self.w//2, 100)))

        for i, name in enumerate(self.maps):
            color = (255, 255, 255) if i == self.selected else (150, 150, 150)
            surf = self.font.render(name, True, color)
            self.screen.blit(surf, (100, 180 + i * 40))
