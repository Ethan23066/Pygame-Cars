@echo off
echo === Pygame Cars - Setup Windows ===

python -m venv .venv
call .venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Setup termine
echo Lance le jeu avec : python main.py
pause
