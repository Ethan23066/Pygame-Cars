import pygame
from ui import MainMenu
from select_map import SelectMap
from select_sprite import SelectSprite
from game import Game
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    # -------- STATE --------
    state = "MENU"
    selected_map = None
    selected_sprite = None

    # -------- TIME SCALE (TEST MODE) --------
    time_scale = 1.0  # 0.5 = slow | 1.0 = normal | 2.0 = fast test

    # -------- UI --------
    menu = MainMenu(screen)
    select_map = SelectMap(screen)
    select_sprite = SelectSprite(screen)

    game = None
    running = True

    while running:
        raw_dt = clock.tick(FPS) / 1000.0
        dt = raw_dt * time_scale   # 🔥 ICI le boost de test

        # -------- EVENTS --------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # --- TIME SCALE CONTROLS ---
                if event.key == pygame.K_F1:
                    time_scale = 0.5
                elif event.key == pygame.K_F2:
                    time_scale = 1.0
                elif event.key == pygame.K_F3:
                    time_scale = 2.0

            if state == "MENU":
                result = menu.handle_event(event)
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
            game.update(dt)
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
