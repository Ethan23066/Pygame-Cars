import pygame
import pygame

class GamepadController:
    def __init__(self):
        pygame.joystick.init()
        self.j = None

        if pygame.joystick.get_count() > 0:
            self.j = pygame.joystick.Joystick(0)
            self.j.init()
            print("🎮 Manette détectée :", self.j.get_name())
        else:
            print("❌ Aucune manette détectée")

    def get_input(self):
        # OBLIGATOIRE pour mettre à jour les axes
        pygame.event.pump()

        if not self.j:
            return {
                "left": False,
                "right": False,
                "accelerate": False,
                "brake": False
            }

        # EasySMX X15 (XInput-like)
        turn = self.j.get_axis(0)      # joystick gauche X
        brake = self.j.get_axis(2)     # LZ / LT
        accel = self.j.get_axis(5)     # RZ / RT

        # Deadzone
        DEADZONE = 0.3

        return {
            "left": turn < -DEADZONE,
            "right": turn > DEADZONE,
            "accelerate": accel > 0.2,
            "brake": brake > 0.2
        }
