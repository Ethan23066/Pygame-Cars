# select_control.py
from control_keyboard import KeyboardController
from control_gamepad import GamepadController

def select_control(mode="keyboard"):
    if mode == "keyboard":
        return KeyboardController()
    elif mode == "gamepad":
        return GamepadController()
    else:
        raise ValueError(f"Unknown control mode: {mode}")
