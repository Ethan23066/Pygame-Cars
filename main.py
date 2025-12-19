import pygame

from game import Game
from select_map import SelectMap
from select_sprite import SelectSprite


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Cars")
    clock = pygame.time.Clock()

    # -------- STATES --------
    state = "SELECT_MAP"
    selected_map = None
    selected_sprite = None

    select_map = SelectMap(screen)
    select_sprite = SelectSprite(screen)

    game = None
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # -------- SELECT MAP --------
            if state == "SELECT_MAP":
                result = select_map.handle_event(event)
                if result:
                    selected_map = result
                    state = "SELECT_SPRITE"

            # -------- SELECT SPRITE --------
            elif state == "SELECT_SPRITE":
                result = select_sprite.handle_event(event)
                if result:
                    selected_sprite = result

                    game = Game()
                    game.set_map(selected_map)
                    game.set_sprite(selected_sprite)

                    state = "GAME"

        # -------- DRAW --------
        if state == "SELECT_MAP":
            select_map.draw()

        elif state == "SELECT_SPRITE":
            select_sprite.draw()

        elif state == "GAME":
            game.run()
            running = False  # fin du jeu après la partie

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
