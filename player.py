from kart import Kart_125_cc

class Player:
    def __init__(self, x, y, image, controller):
        self.kart = Kart_125_cc(x, y, image)
        self.controller = controller
        self.score = 0
        self.health = 100

    def update(self):
        control_input = self.controller.get_input()
        self.kart.update(control_input)

    def draw(self, screen):
        screen.blit(self.kart.image, self.kart.rect)
