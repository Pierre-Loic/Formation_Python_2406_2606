# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Créer une liste vide
# - Lire les instructions présentées dans la chaine de caractères actions_liste
# - Appliquer ces actions à la liste vide créée initialement
# ______
# RESULTATS
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

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
list_1 = list()
list_1.insert(0, 5)
list_1.insert(1, 10)
list_1.insert(0, 6)
print(list_1)
list_1.remove(6)
list_1.append(9)
list_1.append(1)
list_1.sort()
print(list_1)
list_1.pop()
list_1.reverse()
print(list_1)
