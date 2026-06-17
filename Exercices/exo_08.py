from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═════════╗\n' +
    '║^        ║\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║ X  XX  X║\n' +
    '╚═════════╝',

    # tableau attendu.
    '╔═════════╗\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║X  XX  X ║\n' +
    '╚═════════╝'
)


# ------> Enoncé :

# décale les crois a gauche.

# parcourt le tableau de gauche a droite, a chaque colonne vérifie si il y a un block, et déplace le a gauche.
# pour cela tu peu utiliser "if" et "hauteurColonne()".

# example :
# if hauteurColonne() == 1:    # si la colonne contien un block ...
#     prendre()                # ... prend le.


# ------> solution ci-dessous.























# ------> solution.

while positionDuGrappin() != 9:    # répète tant que le grappin n'est pas sur la colonne 9 ...
    droite()                       # ... aller a droite.

    if hauteurColonne() == 1:      # si la colonne contien un block ...

        prendre()                  # ... décale le a gauche.
        gauche()
        poser()
        droite()
