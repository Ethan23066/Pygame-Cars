import pygame, math

class Kart(pygame.sprite.Sprite):
    def __init__(self, pos=(100,100), sprite=None):
        super().__init__()
        self.original_image = sprite.convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)

        # Physique
        self.angle = 0.0
        self.speed = 0.0
        self.accel = 0.4
        self.friction = 0.08
        self.turn_speed = 3.0
        self.max_speed = 8.0

    def update(self, keys):
        # Rotation gauche/droite
        if keys[pygame.K_LEFT]:
            self.angle += self.turn_speed
        if keys[pygame.K_RIGHT]:
            self.angle -= self.turn_speed

        # Avancer (flèche ↑)
        if keys[pygame.K_UP]:
            self.speed = min(self.max_speed, self.speed + self.accel)
        else:
            # friction naturelle
            if self.speed > 0:
                self.speed = max(0, self.speed - self.friction)

        # Déplacement selon angle
        rad = math.radians(self.angle)
        dx = math.cos(rad) * self.speed
        dy = math.sin(rad) * self.speed
        self.rect.centerx += dx
        self.rect.centery += dy

        # Rotation visuelle
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1.0)
        self.rect = self.image.get_rect(center=self.rect.center)
