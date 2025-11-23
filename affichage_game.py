# affichage_game.py
import pygame
import settings

def draw_game(screen, player_rect, current_map=None):
    """
    Affiche le jeu :
    - Fond
    - Map (si chargée)
    - Joueur
    """
    # Fond
    screen.fill(settings.COLOR_BG)

    # Map (optionnel, si tu utilises pytmx plus tard)
    if current_map:
        # Exemple : dessiner une grille simple pour debug
        for x in range(0, settings.WINDOW_WIDTH, settings.TILE_SIZE):
            pygame.draw.line(screen, settings.COLOR_GRID, (x, 0), (x, settings.WINDOW_HEIGHT))
        for y in range(0, settings.WINDOW_HEIGHT, settings.TILE_SIZE):
            pygame.draw.line(screen, settings.COLOR_GRID, (0, y), (settings.WINDOW_WIDTH, y))

    # Joueur
    pygame.draw.rect(screen, settings.COLOR_PLAYER, player_rect)

    # Rafraîchissement
    pygame.display.flip()
