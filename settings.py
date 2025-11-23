# settings.py

# --- Fenêtre ---
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE  = "Pygame Cars"

# --- Performance ---
FPS = 60
MEMORY_LIMIT_MB = 512   # discipline capsule : limite RAM

# --- Sprites ---
SPRITE_SIZE = 100        # largeur/hauteur des sprites
PLAYER_SPEED = 5         # vitesse de base du joueur

# --- Map ---
TILE_SIZE = 16           # taille d'une tuile
MAPS_DIR = "maps/"       # dossier spécial pour les .tmx
MAP_FILE = MAPS_DIR + "map_unique.tmx"

# Exemple de dimensions si tu veux une map géante
MAP_WIDTH_TILES  = 160   # largeur en tiles
MAP_HEIGHT_TILES = 120   # hauteur en tiles
# => map totale = 160 * 16 = 2560 px de large
# => map totale = 120 * 16 = 1920 px de haut

# --- Couleurs ---
COLOR_BG     = (30, 30, 30)      # fond
COLOR_GRID   = (50, 50, 50)      # grille
COLOR_PLAYER = (200, 50, 50)     # joueur

# --- Fichiers ---
ASSETS_DIR = "assets/"
