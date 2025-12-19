import pygame

class SelectSprite:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.karts = ["Kart125CC"]  # extensible
        self.selected = 0
        self.w, self.h = screen.get_size()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.karts)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.karts)
            elif event.key == pygame.K_RETURN:
                return self.karts[self.selected]
            elif event.key == pygame.K_ESCAPE:
                return "BACK"
        return None

    def draw(self):
        self.screen.fill((10, 10, 10))
        title = self.font.render("Choisir un kart", True, (200, 200, 200))
        self.screen.blit(title, title.get_rect(center=(self.w//2, 100)))

        for i, kart in enumerate(self.karts):
            color = (255, 255, 255) if i == self.selected else (150, 150, 150)
            surf = self.font.render(kart, True, color)
            self.screen.blit(surf, (100, 180 + i * 40))
