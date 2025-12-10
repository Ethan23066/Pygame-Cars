import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from pytmx import TiledMap
import numpy as np

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glEnable(GL_TEXTURE_2D)

    # Charger la map TMX
    tmx_data = TiledMap("maps/Race01_kart.tmx")

    # Exemple : transformer un calque en matrice numpy
    layer = tmx_data.layers[0]  # premier calque
    grid = np.array([[layer.data[y][x] for x in range(tmx_data.width)]
                     for y in range(tmx_data.height)])

    print("Grille numpy shape:", grid.shape)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Afficher la map entière
        for y in range(tmx_data.height):
            for x in range(tmx_data.width):
                tile_id = grid[y, x]
                if tile_id != 0:
                    image = tmx_data.get_tile_image_by_gid(tile_id)
                    if image:
                        w, h = image.get_size()
                        data = pygame.image.tostring(image, "RGBA", True)
                        tex_id = glGenTextures(1)
                        glBindTexture(GL_TEXTURE_2D, tex_id)
                        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
                                     GL_RGBA, GL_UNSIGNED_BYTE, data)

                        px, py = x * tmx_data.tilewidth, y * tmx_data.tileheight
                        glBegin(GL_QUADS)
                        glTexCoord2f(0, 0); glVertex2f(px, py)
                        glTexCoord2f(1, 0); glVertex2f(px+w, py)
                        glTexCoord2f(1, 1); glVertex2f(px+w, py+h)
                        glTexCoord2f(0, 1); glVertex2f(px, py+h)
                        glEnd()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
