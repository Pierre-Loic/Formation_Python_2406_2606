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

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"


def cesar_encode(message, nombre):
    list_char = list(message)
    texte_chiffre = ''
    for elmt in list_char:
        new_char = alphabet.find(elmt) + nombre
        nombre += 1
        module = int(new_char) % len(alphabet)
        texte_chiffre = texte_chiffre + str(alphabet[module])
        pass
    return texte_chiffre


def cesar_decode(message, nombre):
    list_char = list(message)
    texte_chiffre = ''
    for elmt in list_char:
        new_char = alphabet.find(elmt) - nombre
        nombre += 1
        module = int(new_char) % len(alphabet)
        texte_chiffre = texte_chiffre + str(alphabet[module])
        pass
    return texte_chiffre


def rotor_encode(message, rotor):
    list_char = list(message)
    texte_chiffre = ''
    for elmt in list_char:
        new_char = alphabet.find(elmt)
        module = int(new_char) % len(rotor)
        texte_chiffre = texte_chiffre + str(rotor[module])
        pass
    return texte_chiffre


def rotor_decode(message, rotor):
    list_char = list(message)
    texte_chiffre = ''
    for elmt in list_char:
        new_char = rotor.find(elmt)
        module = int(new_char) % len(alphabet)
        texte_chiffre = texte_chiffre + str(alphabet[module])
        pass
    return texte_chiffre


def encode(rotor1, rotor2, rotor3, message, nombre):
    message = cesar_encode(message, nombre)
    print(message)
    message = rotor_encode(message, rotor1)
    print(message)
    message = rotor_encode(message, rotor2)
    print(message)
    message = rotor_encode(message, rotor3)
    print(message)
    return message


def decode(rotor1, rotor2, rotor3, message, nombre):
    message = rotor_decode(message, rotor3)
    print(message)
    message = rotor_decode(message, rotor2)
    print(message)
    message = rotor_decode(message, rotor1)
    print(message)
    message = cesar_decode(message, nombre)
    print(message)
    return message


mess_1 = encode(rotor1, rotor2, rotor3, "AAA", 4)
decode(rotor1, rotor2, rotor3, mess_1, 4)
