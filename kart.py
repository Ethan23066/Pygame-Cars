import pygame
import math


class Kart125CC(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        # --- Image ---
        self.original_image = pygame.transform.smoothscale(image, (60, 60))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        # --- Position ---
        self.pos = pygame.Vector2(x, y)

        # --- Mouvement ---
        self.angle = 0.0          # degrés
        self.speed = 0.0

        # --- Réglages (dt-safe) ---
        self.max_speed = 240.0
        self.acceleration = 40.0
        self.brake_force = 50.0
        self.friction = 1.0
        self.rotation_speed = 30.0
        self.turn_drag = 50.0


    def update(self, actions, dt):
        turning = False

        # --- Accélération / frein ---
        if actions.get("accelerate", False):
            self.speed -= self.acceleration * dt
        elif actions.get("brake", False):
            self.speed += self.brake_force * dt
        else:
            if self.speed > 0:
                self.speed -= self.friction * dt
                if self.speed < 0:
                    self.speed = 0
            elif self.speed < 0:
                self.speed += self.friction * dt
                if self.speed > 0:
                    self.speed = 0

        # --- Clamp vitesse ---
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))

        # --- Rotation (uniquement si le kart roule) ---
        if abs(self.speed) > 0.2:
            if actions.get("left", False):
                self.angle += self.rotation_speed * dt
                turning = True
            if actions.get("right", False):
                self.angle -= self.rotation_speed * dt
                turning = True

        # --- Ralentissement en virage ---
        if turning:
            ratio = abs(self.speed) / self.max_speed
            self.speed -= self.turn_drag * ratio * dt * (1 if self.speed > 0 else -1)

        # --- Déplacement ---
        rad = math.radians(self.angle)
        direction = pygame.Vector2(-math.sin(rad), -math.cos(rad))
        self.pos += direction * self.speed * dt

        # --- Rotation visuelle ---
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)
