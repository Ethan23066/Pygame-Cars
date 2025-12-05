import os
import xml.etree.ElementTree as ET

def parse_tsx(tsx_path):
    tree = ET.parse(tsx_path)
    root = tree.getroot()
    tilewidth = int(root.get("tilewidth"))
    tileheight = int(root.get("tileheight"))
    image = root.find("image")
    source = image.get("source")
    width = int(image.get("width"))
    height = int(image.get("height"))

    # chemin complet vers le PNG
    tsx_dir = os.path.dirname(tsx_path)
    png_path = os.path.join(tsx_dir, source)

    # calcul du nombre de colonnes/lignes
    cols = width // tilewidth
    rows = height // tileheight

    return {
        "png": os.path.normpath(png_path),
        "tilewidth": tilewidth,
        "tileheight": tileheight,
        "cols": cols,
        "rows": rows
    }

# Exemple
info = parse_tsx("maps/road.tsx")
print(info)
