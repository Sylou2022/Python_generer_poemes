import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from V.visual import startup

# Démarrage du programme
startup()

#Mode d'emploi du script de poeme
#1erment start.py
#la page option s'affiche
#Je  peux afficher les options avec show_dom
#La syntaxe pour afficher une option est DOM=Option 