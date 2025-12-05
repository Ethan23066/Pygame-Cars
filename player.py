# player.py
import settings
import assets

class Player:
    def __init__(self, start_pos=(100, 100), sprite_file="car.png"):
        # Charger le sprite PNG du joueur
        self.image = assets.load_png(sprite_file)
        self.rect = self.image.get_rect(topleft=start_pos)
        self.speed = settings.PLAYER_SPEED

    def update(self, controller):
        """
        Met à jour la position du joueur selon le contrôleur actif
        (keyboard ou gamepad).
        """
        self.rect = controller.update(self.rect)

    def draw(self, surface):
        """Affiche le joueur sur l'écran."""
        surface.blit(self.image, self.rect)
