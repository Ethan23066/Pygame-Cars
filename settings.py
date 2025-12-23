# settings.py

# --- Fenêtre ---
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE  = "Pygame Cars"

# --- Performance ---
FPS = 30
MEMORY_LIMIT_MB = 512   # discipline capsule : limite RAM

# --- Sprites ---
SPRITE_SIZE = 100        # largeur/hauteur des sprites

# --- Map ---
TILE_SIZE = 100           # taille d'une tuile
MAPS_DIR = "maps/"       # dossier spécial pour les .tmx
MAP_FILE = MAPS_DIR + "map_unique.tmx"

# Exemple de dimensions si tu veux une map géante
MAP_WIDTH_TILES  = 160   # largeur en tiles
MAP_HEIGHT_TILES = 120   # hauteur en tiles
# => map totale = 160 * 100 = 2560 px de large
# => map totale = 120 * 100 = 1920 px de haut

# --- Couleurs ---
COLOR_BG     = (30, 30, 30)      # fond
COLOR_GRID   = (50, 50, 50)      # grille
COLOR_PLAYER = (200, 50, 50)     # joueur

# --- Fichiers ---
ASSETS_DIR = "assets/"


# --- Debug / Test ---
DEBUG_MODE = True
TIME_SCALE = 1.0   # 1.0 = normal | 2.0 = jeu x2 (test)
