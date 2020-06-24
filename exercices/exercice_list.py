# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Manipuler la chaine de caractères liste_node pour créer une liste de liste
# de la forme suivante : [["Emma", 20], ...]
# - Trier la liste par ordre décroissant de notes
# - Calculer la moyenne des notes
#test
def takeSecond(elem):
    return elem[1]
liste_notes = """
Emma
20
Gabriel
18
Jade
17
Louise
20
Raphael
17
Léo
16
"""
liste_notes = liste_notes.split()
liste_eleve = liste_notes[0:12:2]
liste_notes = liste_notes[1:12:2]
liste_tot =[]
for i, name in enumerate(liste_eleve):
    liste_tot.append([name, liste_notes[i]])

liste_tot.sort(key=takeSecond, reverse=True)
print(liste_tot)
