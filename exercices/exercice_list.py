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
list_1 = liste_notes.split("\n")

# Init var
list_2 = list()
list_3 = list()
sum_note = 0
nb_note = 0

for elmt in list_1:
    # Remove empty
    if elmt:
        if elmt.isdigit():
            sum_note += int(elmt)
            nb_note += 1
            list_3.append(int(elmt))
        else:
            list_3 = [elmt, ]
            list_2.append(list_3)
            pass
        pass
    pass

print("La Liste:")
print(list_2)
print(sorted(list_2, key=lambda liste: liste[1]))

print("La moyenne est de:")
print(sum_note / nb_note)
