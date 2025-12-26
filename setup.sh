#!/bin/bash
set -e

echo "=== Pygame Cars - Setup Linux ==="

# Vérifie python3
command -v python3 >/dev/null || {
  echo "❌ python3 non trouvé"
  exit 1
}

# Crée le venv si absent
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Active le venv
source .venv/bin/activate

# Toujours utiliser le pip du venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo
echo "Setup termine"
echo "Lance le jeu avec : python main.py"

