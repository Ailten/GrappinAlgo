
from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═══════════╗\n' +
    '║^          ║\n' +
    '║           ║\n' +
    '║           ║\n' +
    '║#          ║\n' +
    '╚═══════════╝',

    # tableau attendu.
    '╔═══════════╗\n' +
    '║           ║\n' +
    '║           ║\n' +
    '║           ║\n' +
    '║          #║\n' +
    '╚═══════════╝'
)


# ------> Enoncé :

# prend le block avec le grappin.
# et déplace le tout a droite du tableau (10 fois a droite).
# pour cela, utiliser une boucle "for _ in range(10):"
# en suite pose le.

# pour cela tu aura besoin d'une boucle "for".
# (for permet de dire "répète une suite d'instruction N fois")


# ------> solution ci-dessous.























# ------> solution.

prendre()  # demande au grappin de déssendre pour prendre un block.
for _ in range(10):  # répète 10 fois ...
    droite()         # ... aller a droite.
poser()  # demande au grappin de poser le block qu'il porte.