# camera.py
import pyscroll

class CameraManager:
    def __init__(self, tmx_data, screen_size, zoom=1):
        """
        Initialise le renderer et le groupe pyscroll.
        - tmx_data : map chargée avec pytmx.load_pygame()
        - screen_size : (width, height) de la fenêtre
        - zoom : facteur de zoom (1 = normal)
        """
        self.map_layer = pyscroll.BufferedRenderer(tmx_data, screen_size)
        self.map_layer.zoom = zoom

        # Groupe pyscroll qui gère les sprites + caméra
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

    def add(self, sprite):
        """Ajoute un sprite (joueur, NPC, etc.) au groupe."""
        self.group.add(sprite)

    def update(self, target_rect_center):
        """Centre la caméra sur la position du sprite cible."""
        self.group.center(target_rect_center)

    def draw(self, surface):
        """Dessine la map + les sprites sur la surface donnée."""
        self.group.draw(surface)
