from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═════════╗\n' +
    '║^        ║\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║        X║\n' +
    '╚═════════╝',

    # tableau attendu.
    '╔═════════╗\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║         ║\n' +
    '║X        ║\n' +
    '╚═════════╝'
)


# ------> Enoncé :

# ramener la crois a gauche.

# tu a déja fait cette exercice précédement, l'objectif cette fois est de créer tes propre fonctions.
# une fonction est une suite d'instruction que l'on peu appeler a diférent endroit.
# le but d'une fonction est de créer une ligne de code qui fera une suite d'instruction prévue.

# crée une fonction "allerADroiteJusqua()" et "allerAGaucheJusqua()", qui déplacera le grappin a droite ou a gauche jusqu'a la colonne souhaitée.
# pour créer tes propre fonction tu aura besoin d'utiliser "def".
# example :
# def ma_fonction(ma_variable):    # crée une fonction (qui prend un parametre).
#     if ma_variable == 1:         # (dans la fonction) si mon parametre donné est 1 ...
#         droite()                 # (dans la fonction) ... alor va a droite.


# indice :
# tu peu placer des boucle "while" dans une fonction.


# ------> solution ci-dessous.























# ------> solution.

def allerADroiteJusqua(colonne_destination):            # crée une fonction qui permet d'aller a droite jusqu'a la colonne demandée.
    while positionDuGrappin() < colonne_destination:
        droite()

def allerAGaucheJusqua(colonne_destination):            # crée une fonction qui permet d'aller a gauche jusqu'a la colonne demandée.
    while positionDuGrappin() > colonne_destination:    # attention, il fau invercer le sence de comparaison.
        gauche()                                        # attention, il fau aller a gauche cette fois ci.

allerADroiteJusqua(9)          # appeler la fonction créer.
prendre()
allerAGaucheJusqua(1)
poser()


# il est également possible de créer une fonction qui "allerALaColonne()" qui permétré d'aller a gauche ou a droite en comparent la position du grappin avec la colonne de destination.
# tu aura alor une fonction que tu peu appeler pour aller a droite ou a gauche, intéligement.
