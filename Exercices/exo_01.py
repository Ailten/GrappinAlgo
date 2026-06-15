from GrappinAlgo import *

makeExercice(

    # tableau de départ.
    '╔════════╗\n' +
    '║   ^    ║\n' +
    '║        ║\n' +
    '║        ║\n' +
    '║   #    ║\n' +
    '╚════════╝',

    # tableau attendu.
    '╔════════╗\n' +
    '║        ║\n' +
    '║        ║\n' +
    '║        ║\n' +
    '║     #  ║\n' +
    '╚════════╝'
)


# ------> Enoncé :

# prend le block avec le grappin.
# et déplace le de 2 colonne sur la droite.
# en suite pose le.

# pour cela tu aura besoin de la fonction "prendre()", "droite()" et "poser()".


# ------> solution ci-dessous.























# ------> solution.

prendre()  # demande au grappin de déssendre pour prendre un block.
droite()  # déplace le grappin sur la droite, (une première fois).
droite()  # déplacer a nouveau le grappin, (une seconde fois)
poser()  # demande au grappin de poser le block qu'il porte.