import pygame

class GamepadController:
    def __init__(self):
        pygame.joystick.init()
        self.j = pygame.joystick.Joystick(0) if pygame.joystick.get_count() else None
        if self.j: self.j.init()

    def get_input(self):
        if not self.j: return {"up":0,"down":0,"left":0,"right":0}
        ax = self.j.get_axis
        return {"up":ax(1)<-0.5,"down":ax(1)>0.5,"left":ax(0)<-0.5,"right":ax(0)>0.5}
