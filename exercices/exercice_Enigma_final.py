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

nombre = 4
rotors = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    ]
message = "ABC"


def encode(rotors, message, nombre):
    result = ""
    for i, letter in enumerate(message):
        result += rotors[0][(rotors[0].index(letter)+nombre+i)%26]
    for rotor in rotors[1:]:
        new_result = ""
        for i, letter in enumerate(result):
            new_result += rotor[rotors[0].index(letter)]
        result = new_result
    return result

def decode(rotors, message, nombre):
    result = message
    for rotor in rotors[:0:-1]:
        new_result = ""
        for i, letter in enumerate(result):
            new_result += rotors[0][rotor.index(letter)]
        result = new_result
    new_result = ""
    for i, letter in enumerate(result):
        new_result += rotors[0][(rotors[0].index(letter)-nombre-i)%26]
    return new_result

print(encode(rotors, message, nombre))
print(decode(rotors, encode(rotors, message, nombre), nombre))