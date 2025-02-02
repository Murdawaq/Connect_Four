from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from Model.Joueur import *
from random import randint
from random import choice

# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")
print("\n")

def toStringPlateau(plateau):
    """
    Fonction permettant d'afficher un plateau de puissance 4 dans la console

    :param plateau: Plateau que l'on veut transformer en chaîne de caractères (mode graphique)
    :return: Retourne le plateau en chaîne de caractères
    """
    res = ""

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] is not None and plateau[i][j].get(const.COULEUR) == 1:
                res += "|" + "\x1B[41m \x1B[0m"
            elif plateau[i][j] is not None and plateau[i][j].get(const.COULEUR) == 0:
                res += "|" + "\x1B[43m \x1B[0m"
            else:
                res += "|" + " "
        res += "|\n"

    for i in range(len(plateau[0]) * 2 + 1):
        res += "-"
    res += "\n"

    for i in range(len(plateau[0])):
        res += " " + str(i)

    return res

v2 = construirePlateau()
for _ in range(20):
 placerPionPlateau(v2, construirePion(const.ROUGE),
 randint(0, const.NB_COLUMNS - 1))
#print(toStringPlateau(p))


#print(detecter4verticalPlateau(p, const.JAUNE))
#print(detecter4diagonaleDirectePlateau(p, const.JAUNE))
#print(detecter4diagonaleIndirectePlateau(p, const.JAUNE))
#print(getPionsGagnantsPlateau(p))
#print(isRempliPlateau(p))
print(toStringPlateau(v2))
print(detecter3horizontalIA(v2, const.JAUNE))
print(detecter3diagonaleDirecteIA(v2, const.JAUNE))