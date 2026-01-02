import pygame

# ------------------------------
# Types de terrain
# ------------------------------
TILE_WALL = 1
TILE_OUT  = 2
TILE_RACE = 3

class CollisionMap:
    def __init__(self, collision_image_path):
        """Charge une image de collision basée sur les couleurs"""
        self.img = pygame.image.load(collision_image_path).convert()
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def get_tile(self, x, y):
        """Retourne le type de terrain selon la couleur du pixel"""

        # Hors limites = mur
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return TILE_WALL

        color = self.img.get_at((int(x), int(y)))[:3]

        # BLEU = WALL
        if color == (0, 0, 255):
            return TILE_WALL

        # VERT = OUT OF RACE
        if color == (0, 255, 0):
            return TILE_OUT

        # GRIS = RACE
        if color in [(128, 128, 128), (127, 127, 127), (129, 129, 129)]:
            return TILE_RACE

        # Par défaut : piste
        return TILE_RACE

    def is_road(self, x, y):
        return self.get_tile(x, y) == TILE_RACE

    def friction(self, x, y):
        tile = self.get_tile(x, y)

        if tile == TILE_RACE:
            return 1.0
        if tile == TILE_OUT:
            return 0.6
        if tile == TILE_WALL:
            return 0.0

        return 1.0

    def speed_modifier(self, x, y):
        tile = self.get_tile(x, y)

        if tile == TILE_RACE:
            return 1.0
        if tile == TILE_OUT:
            return 0.7
        if tile == TILE_WALL:
            return 0.0

        return 1.0
