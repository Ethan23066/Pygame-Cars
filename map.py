# map.py
import pytmx
import os
import pyscroll

class MapManager:
    def __init__(self, maps_dir="maps"):
        """
        Gère le chargement des maps .tmx depuis le dossier map/.
        """
        self.maps_dir = maps_dir
        self.loaded_maps = {}

    def load_map(self, filename):
        """
        Charge une map .tmx et la garde en cache.
        """
        path = os.path.join(self.maps_dir, filename)
        if filename not in self.loaded_maps:
            tmx_data = pytmx.load_pygame(path, pixelalpha=True)
            self.loaded_maps[filename] = tmx_data
        return self.loaded_maps[filename]

    def create_camera(self, filename, screen_size, zoom=1):
        """
        Charge une map et retourne un CameraManager prêt à l’emploi.
        """
        tmx_data = self.load_map(filename)
        map_layer = pyscroll.BufferedRenderer(tmx_data, screen_size)
        map_layer.zoom = zoom
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        return group
