
from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═══════╗\n' +
    '║^      ║\n' +
    '║       ║\n' +
    '║OOO    ║\n' +
    '║OOO    ║\n' +
    '║OOO    ║\n' +
    '╚═══════╝',

    # tableau attendu.
    '╔═══════╗\n' +
    '║       ║\n' +
    '║       ║\n' +
    '║    OOO║\n' +
    '║    OOO║\n' +
    '║    OOO║\n' +
    '╚═══════╝'
)


# ------> Enoncé :

# encore plus de rond.
# cette fois ci il y a plusieurs étage a chaque colone.
# tu va devoir prendre et déposer 3 fois pour chaque colonne.
# une boucle devrais aider pour cela aussi.


# ------> solution ci-dessous.























# ------> solution.

for _ in range(3):         # cette boucle permet de répéter le placement d'une ligne de rond 3 fois.

    for _ in range(3):          # cette boucle permet de placer une ligne de rond.
        prendre() 
        for _ in range(4):
            droite()
        poser() 
        for _ in range(4):
            gauche()
        droite()

    gauche()   # a la fin d'une ligne, le grappin fini a droite, il fau donc le ramener au début de la prochaine ligne de rond.
    gauche()
    gauche()


# (cette exercice peu etre fait de plusieurs fasson, félicitation si tu a trouvé une méthode diférente).