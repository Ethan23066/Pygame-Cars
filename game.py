import pygame
from select_control import select_controller
from map import MapManager
from assets import load_png
import pytmx

class Camera:
    def __init__(self, width, height):
        self.x, self.y = 0, 0
        self.width, self.height = width, height

    def apply(self, rect):
        """Décale un rect selon la position caméra"""
        return rect.move(-self.x, -self.y)

    def update(self, target_pos):
        """Centre la caméra sur la position du joueur"""
        self.x = target_pos[0] - self.width // 2
        self.y = target_pos[1] - self.height // 2


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame Cars")

        # Charger la map
        maps = MapManager("maps")
        self.tmx_data = maps.load_map("Race02_kart.tmx")
        self.tile_w, self.tile_h = self.tmx_data.tilewidth, self.tmx_data.tileheight

        # Créer la caméra maison
        self.camera = Camera(*self.screen.get_size())

        # Charger le joueur
        self.player = pygame.sprite.Sprite()
        self.player.image = load_png("Kart_R2D2KT.png")
        self.player.rect = self.player.image.get_rect(center=(100, 100))

        # Choisir le contrôleur automatiquement
        self.controller = select_controller()

        self.clock = pygame.time.Clock()
        self.running = True

    def draw_map(self):
        """Dessine la map avec offset caméra"""
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        rect = pygame.Rect(x*self.tile_w, y*self.tile_h,
                                           self.tile_w, self.tile_h)
                        self.screen.blit(tile, self.camera.apply(rect))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update joueur (exemple minimal)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.player.rect.y += 5
            if keys[pygame.K_LEFT]:
                self.player.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.player.rect.x += 5

            # Update caméra
            self.camera.update(self.player.rect.center)

            # Dessin
            self.screen.fill((0, 0, 0))
            self.draw_map()
            self.screen.blit(self.player.image, self.camera.apply(self.player.rect))
            pygame.display.flip()

            self.clock.tick(20)

        pygame.quit()
