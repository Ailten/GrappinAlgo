from GrappinAlgo import *

makeExercice(

    # position de départ.
    '╔════════════════╗\n' +
    '║^               ║\n' +
    '║                ║\n' +
    '║                ║\n' +
    '║   #            ║\n' +
    '╚════════════════╝',

    # position d'arrivée.
    '╔════════════════╗\n' +
    '║^               ║\n' +
    '║                ║\n' +
    '║                ║\n' +
    '║            #   ║\n' +
    '╚════════════════╝'
)

# ------> ton code ci-dessous. ▼ ▼ ▼


for _ in range(3):
    droite()
prendre()
for _ in range(9):
    droite()
poser()


# ------> ton code ci-dessus. ▲ ▲ ▲


checkIsExerciceSuccess()

