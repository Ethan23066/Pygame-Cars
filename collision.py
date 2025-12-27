# collision.py
# Règles de collision par tiles
# Source de vérité du monde (mur / herbe / route)

TILE_WALL = 1     # mur (bloquant)
TILE_GRASS = 2    # herbe (ralentit)
TILE_ROAD = 0     # route (normal)

class CollisionMap:
    def __init__(self, tile_map, tile_size):
        """
        tile_map : matrice 2D des tiles
        tile_size : taille d'une tile en pixels
        """
        self.tile_map = tile_map
        self.tile_size = tile_size

    def world_to_tile(self, x, y):
        """Convertit position monde → coordonnées tile"""
        tile_x = int(x // self.tile_size)
        tile_y = int(y // self.tile_size)
        return tile_x, tile_y

    def get_tile(self, x, y):
        """Retourne le type de tile à une position monde"""
        tx, ty = self.world_to_tile(x, y)

        if ty < 0 or ty >= len(self.tile_map):
            return TILE_WALL
        if tx < 0 or tx >= len(self.tile_map[0]):
            return TILE_WALL

        return self.tile_map[ty][tx]

    def is_wall(self, x, y):
        return self.get_tile(x, y) == TILE_WALL

    def is_grass(self, x, y):
        return self.get_tile(x, y) == TILE_GRASS

    def is_road(self, x, y):
        return self.get_tile(x, y) == TILE_ROAD
