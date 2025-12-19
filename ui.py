import pygame

# --------------------
# TEXTES (FR only)
# --------------------
TEXT = {
    "title": "PYGAME CARS",
    "play": "Jouer",
    "options": "Options",
    "quit": "Quitter",
    "back": "Retour",
}

# --------------------
# MENU UI
# --------------------
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()

        self.font_title = pygame.font.Font(None, 64)
        self.font_item = pygame.font.Font(None, 36)

        self.items = [
            TEXT["play"],
            TEXT["options"],
            TEXT["quit"],
        ]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.items)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.items)
            elif event.key == pygame.K_RETURN:
                return self.items[self.selected]
        return None

    def draw(self):
        self.screen.fill((15, 15, 15))

        # Titre
        title_surf = self.font_title.render(TEXT["title"], True, (230, 230, 230))
        self.screen.blit(title_surf, title_surf.get_rect(center=(self.w//2, 100)))

        # Items
        for i, item in enumerate(self.items):
            color = (255, 255, 255) if i == self.selected else (160, 160, 160)
            surf = self.font_item.render(item, True, color)
            rect = surf.get_rect(center=(self.w//2, 220 + i * 50))
            self.screen.blit(surf, rect)
