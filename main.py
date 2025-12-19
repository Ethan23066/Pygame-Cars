import pygame

from ui import MainMenu
from select_map import SelectMap
from select_sprite import SelectSprite
from game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Cars")
    clock = pygame.time.Clock()

    # -------- STATE --------
    state = "MENU"
    selected_map = None
    selected_sprite = None

    # -------- UI --------
    menu = MainMenu(screen)
    select_map = SelectMap(screen)
    select_sprite = SelectSprite(screen)

    game = None
    running = True

    while running:
        clock.tick(30)

        # -------- EVENTS --------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == "MENU":
                result = menu.handle_event(event)
                if result is not None:
                    if result == "PLAY":
                        state = "SELECT_MAP"
                    elif result == "QUIT":
                        running = False

            elif state == "SELECT_MAP":
                result = select_map.handle_event(event)
                if result is not None:
                    selected_map = result
                    state = "SELECT_SPRITE"

            elif state == "SELECT_SPRITE":
                result = select_sprite.handle_event(event)
                if result is not None:
                    selected_sprite = result
                    game = Game(screen, selected_map, selected_sprite)
                    state = "GAME"

            elif state == "GAME":
                game.handle_event(event)

        # -------- UPDATE --------
        if state == "GAME":
            game.update()
            if not game.running:
                running = False

        # -------- DRAW --------
        if state == "MENU":
            menu.draw()
        elif state == "SELECT_MAP":
            select_map.draw()
        elif state == "SELECT_SPRITE":
            select_sprite.draw()
        elif state == "GAME":
            game.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
