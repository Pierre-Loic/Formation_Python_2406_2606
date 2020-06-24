# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Manipuler la chaine de caractères str_node pour créer une liste de liste
# de la forme suivante : [["Emma", 20], ...]
# - Trier la liste par ordre décroissant de notes
# - Calculer la moyenne des notes

str_notes = """
20
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

liste_note = []
for i, elt in enumerate(str_notes.strip('\n').split('\n')):
    if i%2==0:
        temp_list = [elt]
    else:
        temp_list.insert(0, elt)
        liste_note.append(temp_list)
print(liste_note)
liste_note.sort(key=lambda x: x[1], reverse=True)
print(liste_note)
moyenne = round(sum([int(x[1]) for x in liste_note])/len(liste_note), 2)
print(f"La moyenne de la classe est de {moyenne}")