import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import *
import csv

TILE_SIZE = 100
VIEWPORT_W, VIEWPORT_H = 800, 600

def load_texture(path):
    """Charge une image en texture OpenGL"""
    surf = pygame.image.load(path).convert_alpha()
    w, h = surf.get_size()
    data = pygame.image.tostring(surf, "RGBA", True)

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    return tex_id, w, h

def load_csv(path):
    """Charge une map CSV exportée par Tiled"""
    with open(path) as f:
        reader = csv.reader(f)
        grid = [list(map(int, row)) for row in reader]
    return grid

def draw_tile(tex_id, x, y, w, h):
    """Dessine une tile OpenGL"""
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0); glVertex2f(x, y)
    glTexCoord2f(1,0); glVertex2f(x+w, y)
    glTexCoord2f(1,1); glVertex2f(x+w, y+h)
    glTexCoord2f(0,1); glVertex2f(x, y+h)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((VIEWPORT_W, VIEWPORT_H), DOUBLEBUF | OPENGL)

    glEnable(GL_TEXTURE_2D)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, VIEWPORT_W, VIEWPORT_H, 0)  # coord 2D classique
    glMatrixMode(GL_MODELVIEW)

    # Exemple : tileset unique
    tileset, tw, th = load_texture("tileset.png")
    map_grid = load_csv("map.csv")

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Affiche les tiles visibles
        for row_idx, row in enumerate(map_grid):
            for col_idx, tile_id in enumerate(row):
                if tile_id != 0:
                    x = col_idx * TILE_SIZE
                    y = row_idx * TILE_SIZE
                    if x < VIEWPORT_W and y < VIEWPORT_H:
                        draw_tile(tileset, x, y, TILE_SIZE, TILE_SIZE)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
