import pygame
import pytmx

from map import MapManager
from assets import load_png
from kart import Kart125CC


# ---------------- CAMERA ----------------
class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def apply(self, rect):
        return rect.move(-self.x, -self.y)

    def update(self, target_rect):
        self.x = target_rect.centerx - self.width // 2
        self.y = target_rect.centery - self.height // 2


# ---------------- GAME ----------------
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame Cars")

        self.clock = pygame.time.Clock()
        self.running = True

        # --- CHOIX JOUEUR (fallback si non définis) ---
        self.selected_map = None
        self.selected_sprite = None

        # --- MAP ---
        maps = MapManager("maps")
        map_name = self.selected_map or "Race02_kart.tmx"
        self.tmx_data = maps.load_map(map_name)

        self.tile_w = self.tmx_data.tilewidth
        self.tile_h = self.tmx_data.tileheight

        # --- CAMERA ---
        self.camera = Camera(800, 600)

        # --- PLAYER / KART ---
        sprite_name = self.selected_sprite or "Kart_R2D2KT.png"
        kart_image = load_png(sprite_name)
        self.player = Kart125CC(400, 200, kart_image)

        self.all_sprites = pygame.sprite.Group(self.player)

    # -------- CONFIGURATION DEPUIS LE MENU --------
    def set_map(self, map_name):
        self.selected_map = map_name

    def set_sprite(self, sprite_name):
        self.selected_sprite = sprite_name

    # -------- MAP DRAW --------
    def draw_map(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        rect = pygame.Rect(
                            x * self.tile_w,
                            y * self.tile_h,
                            self.tile_w,
                            self.tile_h
                        )
                        self.screen.blit(tile, self.camera.apply(rect))

    # -------- MAIN LOOP --------
    def run(self):
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            # --- UPDATE ---
            keys = pygame.key.get_pressed()
            self.player.update(keys)

            self.camera.update(self.player.rect)

            # --- DRAW ---
            self.screen.fill((0, 0, 0))
            self.draw_map()

            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite.rect))

            pygame.display.flip()

        pygame.quit()


# -------- LAUNCH (debug direct possible) --------
if __name__ == "__main__":
    Game().run()
