import pygame
import pytmx
from map import MapManager
from assets import load_png
from kart import Kart125CC
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from select_control import select_controller


# ---------------- CAMERA ----------------
class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def apply(self, rect):
        return rect.move(-self.x, -self.y)

    def update(self, target_rect, map_width, map_height):
        self.x = target_rect.centerx - self.width // 2
        self.y = target_rect.centery - self.height // 2

        self.x = max(0, min(self.x, map_width - self.width))
        self.y = max(0, min(self.y, map_height - self.height))


# ---------------- GAME ----------------
class Game:
    def __init__(self, screen, map_name, sprite_name):
        self.screen = screen

        # --- MAP ---
        maps = MapManager("maps")
        self.tmx_data = maps.load_map(map_name)
        self.tile_w = self.tmx_data.tilewidth
        self.tile_h = self.tmx_data.tileheight

        self.map_width_px  = self.tmx_data.width  * self.tile_w
        self.map_height_px = self.tmx_data.height * self.tile_h

        # --- CAMERA ---
        self.camera = Camera(WINDOW_WIDTH, WINDOW_HEIGHT)

        # --- PLAYER ---
        kart_image = load_png(sprite_name)
        self.player = Kart125CC(400, 200, kart_image)
        self.all_sprites = pygame.sprite.Group(self.player)

        # --- INPUT ---
        self.controller = select_controller()

        # --- HUD ---
        self.font = pygame.font.SysFont("consolas", 16)

        self.running = True


    # -------- EVENTS --------
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False


    # -------- INPUT (CLAVIER + MANETTE) --------
    def get_actions(self):
        actions = {
            "left": False,
            "right": False,
            "accelerate": False,
            "brake": False
        }

        # --- MANETTE ---
        pad = self.controller.get_input()
        for key in actions:
            actions[key] = pad.get(key, False)

        # --- CLAVIER (fallback sûr) ---
        keys = pygame.key.get_pressed()
        actions["left"] |= keys[pygame.K_LEFT]
        actions["right"] |= keys[pygame.K_RIGHT]
        actions["accelerate"] |= keys[pygame.K_UP]
        actions["brake"] |= keys[pygame.K_DOWN]

        return actions


    # -------- UPDATE --------
    def update(self, dt):
        actions = self.get_actions()
        self.player.update(actions, dt, self.collision_map)
        self.camera.update(
            self.player.rect,
            self.map_width_px,
            self.map_height_px
        )


    # -------- DRAW MAP --------
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


    # -------- HUD --------
    def draw_hud(self):
        speed = abs(self.player.speed)
        speed_txt = self.font.render(
            f"Speed: {int(speed)}",
            True,
            (255, 255, 255)
        )
        self.screen.blit(speed_txt, (10, 10))


    # -------- DRAW --------
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_map()

        for sprite in self.all_sprites:
            self.screen.blit(
                sprite.image,
                self.camera.apply(sprite.rect)
            )

        self.draw_hud()
