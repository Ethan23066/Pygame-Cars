# map.py
import pygame
import settings
import pytmx
import os

class MapManager:
    def __init__(self, maps_dir=settings.MAPS_DIR):
        self.maps_dir = maps_dir
        self.loaded_maps = {}

    def load_map(self, filename):
        """
        Charge une map .tmx depuis le dossier maps/.
        Stocke la map dans loaded_maps pour éviter de recharger.
        """
        path = os.path.join(self.maps_dir, filename)
        if filename not in self.loaded_maps:
            tmx_data = pytmx.load_pygame(path, pixelalpha=True)
            self.loaded_maps[filename] = tmx_data
        return self.loaded_maps[filename]

    def draw_map(self, surface, filename, camera_x=0, camera_y=0):
        """
        Dessine uniquement la portion visible de la map.
        """
        tmx_data = self.load_map(filename)
        tw = settings.TILE_SIZE
        th = settings.TILE_SIZE

        # Limites visibles
        start_x = camera_x // tw
        start_y = camera_y // th
        end_x = (camera_x + settings.WINDOW_WIDTH) // tw + 1
        end_y = (camera_y + settings.WINDOW_HEIGHT) // th + 1

        # Boucle sur les tiles visibles
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer.tiles(start_x, start_y, end_x - start_x, end_y - start_y):
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * tw - camera_x, y * th - camera_y))
