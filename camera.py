import pygame
import pytmx

VIEWPORT_W, VIEWPORT_H = 800, 600

class Camera:
    def __init__(self, width, height):
        self.x, self.y = 0, 0
        self.width, self.height = width, height

    def apply(self, rect):
        """Décale un rect selon la position caméra"""
        return rect.move(-self.x, -self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def main():
    pygame.init()
    screen = pygame.display.set_mode((VIEWPORT_W, VIEWPORT_H))
    clock = pygame.time.Clock()

    # Charger la map Tiled
    tmx_data = pytmx.util_pygame.load_pygame("race_01.tmx")
    tile_w, tile_h = tmx_data.tilewidth, tmx_data.tileheight

    camera = Camera(VIEWPORT_W, VIEWPORT_H)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: camera.move(5, 0)
        if keys[pygame.K_LEFT]:  camera.move(-5, 0)
        if keys[pygame.K_DOWN]:  camera.move(0, 5)
        if keys[pygame.K_UP]:    camera.move(0, -5)

        screen.fill((0,0,0))

        # Dessiner les tiles avec offset caméra
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        rect = pygame.Rect(x*tile_w, y*tile_h, tile_w, tile_h)
                        screen.blit(tile, camera.apply(rect))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
