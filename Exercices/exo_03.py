
from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═══════╗\n' +
    '║^      ║\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║OOO    ║\n' +
    '╚═══════╝',

    # tableau attendu.
    '╔═══════╗\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║    OOO║\n' +
    '╚═══════╝'
)


# ------> Enoncé :

# déplace tout les rond a droite du tableau.
# pour faire ca, tu aura besoin des boucles "for".
# sais tu que tu peu placer une première boucle dans une seconde ?
# n'oublie pas que le grappin doit faire le retour.

# pour cela tu aura besoin d'une boucle "for".

# ------> solution ci-dessous.























# ------> solution.

for _ in range(3):          # répète 3 fois ...
    prendre()               # ... prendre le rond ...
    for _ in range(4):
        droite()            # ... aller 4 fois a droite...
    poser()                 # ... poser le rond ...
    for _ in range(4):
        gauche()            # ... revenir 4 fois a gauche....
    droite()                # ... et ce décaler a droite pour le rond suivant.


# (tu peu aussi améliorer cette vertion en n'allen que 3 fois a gauche pour le retour).