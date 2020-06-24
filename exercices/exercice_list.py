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
tableau_note_base = liste_notes.split()
nb_note = len(tableau_note_base)/2
tableau_note_fin =[]
var = 0
for i,j in enumerate(tableau_note_base):
    if (int(i) % 2) == 0:
        tableau_note_fin.append([tableau_note_base[int(i)], tableau_note_base[int(i) + 1]])
        var =  var +  int(tableau_note_base[int(i) + 1])

print("not sorted" + str(tableau_note_fin))

sorted(tableau_note_fin, key=lambda note: note[1])

print("sorted" + str(tableau_note_fin))

print("moyenne" +var/nb_note)
