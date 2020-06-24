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

import string

message = "AAA"
nombre = 4
rotor1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

def enigma(rotor1, rotor2, rotor3, message, nombre, encode):
    i = nombre
    result = ""
    if encode == True :
        for char in split(message):
            result += rotor(rotor(rotor(cesar(char,i),rotor1,encode),rotor2,encode),rotor3,encode)
            i = i + 1
    else :
        i = i * -1
        for char in split(message):
            result += cesar(rotor(rotor(rotor(char,rotor3,encode),rotor2,encode),rotor1,encode),i)
            i = i - 1
    return result

def rotor(char, rotor, encode):
    if encode == True :
        return rotor[string.ascii_uppercase.index(char)]
    else :
        return string.ascii_uppercase[rotor.index(char)]

def cesar(char, nombre):
    return string.ascii_uppercase[(string.ascii_uppercase.index(char) + nombre) % 26]

def split(word): 
    return [char for char in word.upper()]

code = enigma(rotor1,rotor2,rotor3,"AAA",4, True)
print(code)
print(enigma(rotor1,rotor2,rotor3,code, 4, False))

code = enigma(rotor1,rotor2,rotor3,"ABC",4,True)
print(code)
print(enigma(rotor1,rotor2,rotor3,code,4,False))