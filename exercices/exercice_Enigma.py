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
print("" )
print("exo Enigma ---------------------------------------------" )
print("" )

Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor1 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'

def cesar_encode(parameter,parameter2):
    try:
        cesar_result = ""
        a=0
        b=""
        c=0
        for i in parameter:
            a = ord(i) + parameter2 + c
            b = chr(a)
            c = c + 1
            cesar_result = str(cesar_result) + b

    except TypeError as err:
        print('Handling run-time error:', err)

    return cesar_result

def rotor_encode(Texte,Rotor):
    try:
        rotor_result = ""
        a=0
        for i in Texte:
            a = ord(i)
            rotor_result = rotor_result + Rotor[a-64]

    except TypeError as err:
        print('Handling run-time error:', err)

    return rotor_result

def cesar_decode(parameter,parameter2):
    try:
        cesar_result = ""
        a=0
        b=""
        c=0
        for i in parameter:
            a = ord(i) - parameter2 - c
            b = chr(a)
            c = c + 1
            cesar_result = str(cesar_result) + b

    except TypeError as err:
        print('Handling run-time error:', err)

    return cesar_result

def rotor_decode(Texte,Rotor):
    try:
        rotor_result = ""
        a=0
        b=""
        for i in Texte:

            a = Rotor.index(i)
            print(a)
            b = Letter[a]
            rotor_result = rotor_result + b

    except TypeError as err:
        print('Handling run-time error:', err)

    return rotor_result

def encode(rotor1, rotor2, rotor3, message, nombre):
    result = cesar_encode(message, nombre)
    result = rotor_encode(result, rotor1)
    result = rotor_encode(result, rotor2)
    result = rotor_encode(result, rotor3)
    return result


def decode(rotor1, rotor2, rotor3, message, nombre):
    result = rotor_decode(message, rotor3)
    result = rotor_decode(result, rotor2)
    result = rotor_decode(result, rotor1)
    result = cesar_decode(result, nombre)
    return result


Input_Word: str = str(input("Please enter a word: "))
Input_Size = int(input("Please enter a number: "))



re = str(encode(rotor1, rotor2, rotor3 , Input_Word, Input_Size))
ra = str(decode(rotor1, rotor2, rotor3 , re, Input_Size))
print("coder final // " + re)
print("decoder final// " + ra )
