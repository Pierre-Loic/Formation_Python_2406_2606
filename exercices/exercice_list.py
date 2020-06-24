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
liste_notes = liste_notes.split()
print (liste_notes)

ma_liste = liste_notes[1], liste_notes[3] , liste_notes[5] , liste_notes[7] , liste_notes[9] , liste_notes[11]
ma_liste = list(map(int,ma_liste))
print (sorted(ma_liste))


add = sum(ma_liste)
print(add)
moyenne = add/6

print (moyenne)