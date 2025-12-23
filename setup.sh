#!/bin/bash

echo "=== Pygame Cars setup ==="

# Vérif python
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python3 non trouvé"
    exit 1
fi

# Création venv
if [ ! -d ".venv" ]; then
    echo "➡ Création du venv"
    python3 -m venv .venv
fi

# Activation
echo "➡ Activation du venv"
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install deps
echo "➡ Installation des dépendances"
pip install -r requirements.txt

echo "✅ Setup terminé"
echo "👉 Lance le jeu avec : main.py"
