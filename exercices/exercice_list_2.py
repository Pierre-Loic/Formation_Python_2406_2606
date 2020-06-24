# Notions à utiliser pour résoudre l'exercice :
# listes, boucles, conditions
# ______
# ENONCE
# - Créer une liste vide
# - Lire les instructions présentées dans la chaine de caractères actions_liste
# - Appliquer ces actions à la liste vide créée initialement
def execCommand(cmd,val1,val2):
    if cmd == "insert":
        if val2 is not None:
            empty_list.insert(val1,val2)
        else:
            empty_list.insert(val1)
    elif cmd == "print":
        print(empty_list)
    elif cmd == "remove":
        empty_list.remove(val1)
    elif cmd == "append":
        empty_list.append(val1)
    elif cmd == "sort":
        empty_list.sort()
    elif cmd == "pop":
        empty_list.pop()
    elif cmd == "reverse":
        empty_list.reverse()

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
empty_list = []
actions_liste = actions_liste.split()
tmp_cmd = ""
tmp_val_1 = None
tmp_val_2 = None

for i, val in enumerate(actions_liste):
    if val.isdigit() == False:
        execCommand(tmp_cmd,tmp_val_1,tmp_val_2)
        tmp_cmd = val
        tmp_val_1 = None
        tmp_val_2 = None
    else:
        if tmp_val_1 is None:
            tmp_val_1 = int(val)
        else:
            tmp_val_2 = int(val)
execCommand(tmp_cmd,tmp_val_1,tmp_val_2)