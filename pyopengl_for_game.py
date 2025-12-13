import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class PyOpenGLForGames:
    def __init__(self, screen):
        self.screen = screen
        self.init_gl()

    def init_gl(self):
        glViewport(0, 0, self.screen.get_width(), self.screen.get_height())
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.screen.get_width()/self.screen.get_height()), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

    def draw_example(self):
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-1.0, -1.0, -5.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -5.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 1.0, -5.0)
        glEnd()
