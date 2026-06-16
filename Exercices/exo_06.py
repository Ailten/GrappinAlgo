from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔══════╗\n' +
    '║  ^   ║\n' +
    '║      ║\n' +
    '║      ║\n' +
    '║  OO  ║\n' +
    '║  XX  ║\n' +
    '╚══════╝',

    # tableau attendu.
    '╔══════╗\n' +
    '║      ║\n' +
    '║      ║\n' +
    '║      ║\n' +
    '║  XX  ║\n' +
    '║  OO  ║\n' +
    '╚══════╝'
)


# ------> Enoncé :

# inverce les column.

# pour cela, tu devra les places ailleur temporairement.


# ------> solution ci-dessous.























# ------> solution.

for _ in range(2):    # répète pour les 2 colone.

    prendre()    # place le rond a gauche.
    gauche()
    poser()
    droite()

    prendre()   # place la crois a droite.
    droite()
    poser()
    gauche()

    gauche()    # re-place le rond en premier.
    prendre()
    droite()
    poser()

    droite()    # re-place la croix en premier.
    prendre()
    gauche()
    poser()

    droite()    # déplace le grappin a droite, pour la prochaine colone.