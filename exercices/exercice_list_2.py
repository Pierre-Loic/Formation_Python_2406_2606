# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Créer une liste vide
# - Lire les instructions présentées dans la chaine de caractères actions_liste
# - Appliquer ces actions à la liste vide créée initialement

actions_liste = """
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
liste_vide = []
liste_vide.insert(0, 5)
liste_vide.insert(1,10)
liste_vide.insert(0,6)

print (liste_vide)

liste_vide.remove(6)
liste_vide.append(9)
liste_vide.append(1)

print(sorted(liste_vide))

print(liste_vide.pop(1))

print(sorted(liste_vide,reverse= True))
