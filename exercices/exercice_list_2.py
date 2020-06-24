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

import sys

def Insert(param):
    liste.insert(int(param[1]),int(param[2]))

def Append(param):
    liste.append(int(param[1]))

def Remove(param):
    liste.remove(int(param[1]))

def Sort(param):
    liste.sort()

def Pop(param):
    liste.pop()

def Reverse(param):
    liste.reverse()

def Print(param):
    print(liste)

liste = []
for item in actions_liste.strip('\n').split('\n'):
    getattr(sys.modules[__name__], item.split()[0].capitalize())(item.split())

