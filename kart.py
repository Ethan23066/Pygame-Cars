import pygame
import math

class Kart_125_cc(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        # Images
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

        # Position & mouvement
        self.pos = pygame.Vector2(x, y)
        self.angle = 0.0              # en degrés
        self.speed = 0.0

        # Réglages arcade
        self.max_speed = 8.0
        self.acceleration = 0.15
        self.friction = 0.04
        self.rotation_speed = 3.0

    def update(self, keys):
        # --- Accélération / frein ---
        if keys[pygame.K_UP]:
            self.speed += self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed -= self.acceleration
        else:
            # friction naturelle
            if self.speed > 0:
                self.speed -= self.friction
                if self.speed < 0:
                    self.speed = 0
            elif self.speed < 0:
                self.speed += self.friction
                if self.speed > 0:
                    self.speed = 0

        # Clamp vitesse
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))

        # --- Rotation (dépend de la vitesse) ---
        if abs(self.speed) > 0.1:
            if keys[pygame.K_LEFT]:
                self.angle += self.rotation_speed * (self.speed / self.max_speed)
            if keys[pygame.K_RIGHT]:
                self.angle -= self.rotation_speed * (self.speed / self.max_speed)

        # --- Mouvement avec trigonométrie ---
        rad = math.radians(self.angle)
        direction = pygame.Vector2(-math.sin(rad), -math.cos(rad))
        self.pos += direction * self.speed

        # --- Rotation visuelle ---
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)
