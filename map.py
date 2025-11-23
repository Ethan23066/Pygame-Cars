# map.py
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
