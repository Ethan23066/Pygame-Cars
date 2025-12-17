import pygame
import math

class Kart_125_cc(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.Vector2(x, y)
        self.angle = 0
        self.speed = 0
        self.max_speed = 8
        self.acceleration = 0.9
        self.friction = 0.8
        self.rotation_speed = 5

    def update(self, keys):
        # Contrôle directionnel
        if keys[pygame.K_UP]:
            self.speed += self.acceleration
        if keys[pygame.K_DOWN]:
            self.speed -= self.acceleration
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed

        # Clamp + friction
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))
        self.speed *= self.friction

        # Mouvement dans la direction de l'angle
        dx = -math.sin(math.radians(self.angle)) * self.speed
        dy =  math.cos(math.radians(self.angle)) * self.speed
        self.pos.x += dx
        self.pos.y += dy

        # Rotation visuelle (inversée pour correspondre à l'angle trigonométrique)
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.pos)