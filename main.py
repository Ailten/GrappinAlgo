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

# ------> ton code ci-dessous. ▼ ▼ ▼


prendre()  # demande au grappin de déssendre pour prendre un block.
droite()  # déplace le grappin sur la droite.
droite()
poser()  # demande au grappin de poser le block qu'il porte.


# ------> ton code ci-dessus. ▲ ▲ ▲


checkIsExerciceSuccess()

# ecrit "python3 main.py" dans le terminal pour lancer ton code.

