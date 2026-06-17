from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═════════════╗\n' +
    '║^            ║\n' +
    '║             ║\n' +
    '║    X    X   ║\n' +
    '║ X  X   XXX  ║\n' +
    '║ X  X  XXXX  ║\n' +
    '║ XX XX XXXXX ║\n' +
    '╚═════════════╝',

    # tableau attendu.
    '╔═════════════╗\n' +
    '║             ║\n' +
    '║             ║\n' +
    '║             ║\n' +
    '║             ║\n' +
    '║ XXXXXXXXXXX ║\n' +
    '║ XXXXXXXXXXX ║\n' +
    '╚═════════════╝'
)


# ------> Enoncé :

# répartir les croix.

# pour cela, tu devra parcourir de gauche a droite le tableau.
# a chaque trou rencontré, tu devra "noter" la colonne du grapin (pour y revenir plus tard).
# et re parcourir de zero pour trouver une colonne qui dépassé une hauteur de 2.
# une foi trouvée, prend sont block, retourn au creu que tu a "noté", pose le, et continue jusqu'a l'arrivée.

# variables :
# les variables sont comme des boite, tu peu en créer avec le mot de ton choix (tant que ce n'est pas un mot déja utilisé).
# tu peu te servire de cette boite pour stocker une information a l'intérieur.

# example 1 (remplire la boite) :
# ma_variable = 5       # stock le chiffre 5 dans une variable.

# example 2 (utiliser la boite) :
# if ma_variable == 5:     # si ma variable contien le chiffre 5 ...
#     droite()             # ... va a droite.


# rappel utile / indice :

# pour cela tu aura besoin de "hauteurColonne()" et "positionDuGrappin()" (et "while"):
# example :
# if hauteurColonne() > 1:                   # si la hauteur de la colonne dépasse 1 ...
#     colone_note = positionDuGrappin()      # ... alors, note le numero de la colone.

# example :
# while positionDuGrappin() != colone_note:  # va a droite, tant que le grapin n'est pas sur la colone notée.
#     droite()

# "while" est similaire au "for", il répète une suite d'action tant que la "condition" est respectée.
# dans l'example, "colone_note" est une variable créée, tu peu l'appeler diférament.


# ------> solution ci-dessous.























# ------> solution.

droite()    # commence sur la colonne 2.

while positionDuGrappin() != 13:    # parcourt le tableau de gauche a droite.

    if hauteurColonne() < 2:    # si le grapin est sur une colone qui a besoin d'un block (hauteur inférieur a 2).

        colone_note = positionDuGrappin()    # note la colone ou le grappin est (pour utiliser plus tard).

        while positionDuGrappin() != 2:  # retourne a la colone 2.
            gauche()
        while hauteurColonne() < 3:      # va a droite tant que le grappin n'est pas sur une colonne de 3 ou plus.
            droite()

        prendre()

        while positionDuGrappin() != 2:  # retourne a la colone 2.
            gauche()
        while positionDuGrappin() != colone_note:      # va a droite tant que le grappin n'est pas revenu au "creu".
            droite()

        poser()
    
    droite()    # passe a la colonne suivante.






