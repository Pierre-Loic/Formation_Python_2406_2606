liste_pre = ["Emma","Gabriel","Jade","Louise","Raphael","Leo"]
liste_note =[20,18,17,20,17,16]
for a, b in zip(liste_pre, liste_note):
    print(a,b)
print(sorted(liste_note,reverse=True))
print(sum(liste_note)/6)