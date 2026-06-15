from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔═══════╗\n' +
    '║   ^   ║\n' +
    '║       ║\n' +
    '║   #   ║\n' +
    '║   O   ║\n' +
    '║   O   ║\n' +
    '║   #   ║\n' +
    '╚═══════╝',

    # tableau attendu.
    '╔════════╗\n' +
    '║        ║\n' +
    '║        ║\n' +
    '║        ║\n' +
    '║O      X║\n' +
    '║O      X║\n' +
    '╚════════╝'
)


# ------> Enoncé :

# place les rond a gauche du tablau, et les croix a droite.

# pour cela, tu aura besoin du "if" (si) et de function "blockTenu()" (qui retourn le block que le grappin porte).


# ------> solution ci-dessous.























# ------> solution.

for _ in range(4):           # répète pour les 4 block ...

    prendre()                # ... prendre le block ...
    
    if blockTenu() == 'X':   # ... si c'est une croix, alors ...
        
        for _ in range(3):   # ... le placer a droite ...
            droite()
        poser()
        for _ in range(3):   # ... et revenire.
            gauche()

    if blockTenu() == 'O':   #     si c'est un rond, alors ...

        for _ in range(3):   # ... le placer a gauche ...
            gauche()
        poser()
        for _ in range(3):   # ... et revenire.
            droite()


# (tu peu utiliser "else" pour optimiser).
# (voir meme utiliser le "if" dans les boucle de déplacement).