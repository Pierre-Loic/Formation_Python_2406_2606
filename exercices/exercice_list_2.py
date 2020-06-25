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

result = []
for instruction in actions_liste.split("\n"):
    temp = instruction.split()
    if len(temp)>0:
        if temp[0]=="insert":
            result.insert(int(temp[1]), int(temp[2]))
        elif temp[0]=="print":
            print(result)
        elif temp[0]=="remove":
            result.remove(int(temp[1]))
        elif temp[0]=="append":
            result.append(int(temp[1]))
        elif temp[0]=="sort":
            result.sort()
        elif temp[0]=="pop":
            result.pop()
        elif temp[0]=="reverse":
            result.reverse()
        else:
            print("Erreur")