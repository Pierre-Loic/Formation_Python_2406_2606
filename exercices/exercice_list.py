# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Manipuler la chaine de caractères liste_node pour créer une liste de liste
# de la forme suivante : [["Emma", 20], ...]
# - Trier la liste par ordre décroissant de notes
# - Calculer la moyenne des notes

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
tableau_1 = liste_notes.split("/n")
tableau_2 = []
tableau_3 = []
sum_note = 0
nb_note = 0

for i in tableau_1:
    if i:
        if i.isdigit():
            sum_note += int (i)
            nb_note += 1
            tableau_3.append(int(i))
        else:
            tableau_3 = [i, ]
            tableau_2.append(tableau_3)

print(tableau_2)
print(sorted(tableau_2, key=lambda tableau: tableau[1]))

print("Moyenne : " + (sum_note/nb_note))
