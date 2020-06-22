# Notions à utiliser pour résoudre l'exercice :
# conditions, boucles, chaines de caractères
# ______
# ENONCE
# Durant la seconde guerre mondiale, les allemands utilisaient une machine pour
# chiffrer les messages qu'ils envoyaient. Voici comment elle fonctionnait :
# La première étape est un chiffrement de César avec un nombre incrémental.
# Exemple : si le message est la chaine de caractères AAA et que le nombre de départ est 4
# alors le résultat de cette première étape est EFG.
# A + 4 = E
# A + 4 + 1 = F
# A + 4 + 1 + 1 = G
# Ensuite, le résultat passe dans 3 rotors différents.
# Voici la correspondance du premier rotor :
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# BDFHJLCPRTXVZNYEIWGAKMUSQO
# EFG est ainsi tranformé en JLC
# Voici la correspondance du deuxième rotor :
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# AJDKSIRUXBLHWTMCQGZNPYFVOE
# JLC est ainsi tranformé en BHD.
# Voici la correspondance du troisième rotor :
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# EKMFLGDQVZNTOWYHXUSPAIBRCJ
# BHD est ainsi tranformé en KQF.
# Le résulat final est KQF
#
# Source d'inspiration : Codingame

def encode(rotor1, rotor2, rotor3, message, nombre):
    pass

def decode(rotor1, rotor2, rotor3, message, nombre):
    pass