import pygame
import math


class Kart125CC(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        # --- Image ---
        self.original_image = pygame.transform.smoothscale(image, (80, 80))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        # --- Position ---
        self.pos = pygame.Vector2(x, y)

        # --- Mouvement ---
        self.angle = 0.0          # degrés (0 = vers le haut)
        self.speed = 0.0

        # --- Réglages ---
        self.max_speed = 10.0
        self.acceleration = 0.05
        self.brake_force = 0.02
        self.friction = 0.01
        self.rotation_speed = 2.0
        self.turn_drag = 0.12     # perte de vitesse en virage

    def update(self, keys):
        turning = False

        # --- Accélération / frein ---
        if keys[pygame.K_UP]:
            self.speed -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed += self.brake_force
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

        # --- Rotation (uniquement si on roule) ---
        if abs(self.speed) > 0.2:
            if keys[pygame.K_LEFT]:
                self.angle += self.rotation_speed
                turning = True
            if keys[pygame.K_RIGHT]:
                self.angle -= self.rotation_speed
                turning = True

        # --- Ralentissement en virage ---
        if turning:
            ratio = abs(self.speed) / self.max_speed
            self.speed -= self.turn_drag * ratio * (1 if self.speed > 0 else -1)

        # --- Déplacement ---
        rad = math.radians(self.angle)
        direction = pygame.Vector2(-math.sin(rad), -math.cos(rad))
        self.pos += direction * self.speed

        # --- Rotation visuelle ---
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)
