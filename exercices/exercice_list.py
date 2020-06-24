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
#method 1
listes_1 = []
for i in range(0, len(liste_notes.split()), 2):
    listes_1.append([liste_notes.split()[i], liste_notes.split()[i+1]])

listes_1.sort(key = lambda x: x[1])

print(listes_1)
print(sum(map(int,list(zip(*listes_1))[1]))/len(listes_1))

#method 2
listes_2 = list(map(list,zip(liste_notes.split()[::2],liste_notes.split()[1::2])))
listes_2.sort(key = lambda x: x[1])
print(listes_2)
print(sum(map(int,list(zip(*listes_1))[1]))/len(listes_1))