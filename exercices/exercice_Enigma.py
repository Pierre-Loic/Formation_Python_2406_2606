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

#---------------------------------------------------
#-------------------Encodage------------------------
#---------------------------------------------------

def cesarEncode(message,nombre):
    newMessage = []
    for i,val in enumerate(message):
        iAlphabet = alphabet.index(val)
        iAlphabet = iAlphabet + nombre
        iAlphabet = iAlphabet % 26
        newMessage.append(alphabet[iAlphabet])
        nombre = nombre +1
    return newMessage

def encodeRotor(rotor,message):
    newMessage = []
    for val in message:
        iAlphabet = alphabet.index(val)
        newMessage.append(rotor[iAlphabet])
    return newMessage




#---------------------------------------------------
#-------------------Decodage------------------------
#---------------------------------------------------

def cesarDecode(message,nombre):
    newMessage = []
    
    for i,val in enumerate(message):
        iAlphabet = alphabet.index(val)
        iAlphabet = iAlphabet - nombre
        iAlphabet = iAlphabet % 26
        newMessage.append(alphabet[iAlphabet])
        nombre = nombre + 1
    return newMessage

def decodeRotor(rotor,message):
    newMessage = []
    for val in message:
        iAlphabet = rotor.index(val)
        newMessage.append(alphabet[iAlphabet])
    return newMessage





#---------------------------------------------------
#-------------------Programme-----------------------
#---------------------------------------------------




def encode(rotor1, rotor2, rotor3, message, nombre):
    messageEdit = message.upper()
    messageEdit = list(messageEdit)
    print(messageEdit)
    mes = cesarEncode(messageEdit,nombre)
    print(mes)
    mes = encodeRotor(rotor1,mes)
    print(mes)
    mes = encodeRotor(rotor2,mes)
    print(mes)
    mes = encodeRotor(rotor3,mes)
    print(mes)
    return ''.join(mes)


def decode(rotor1, rotor2, rotor3, message, nombre):
    messageEdit = message.upper()
    messageEdit = list(messageEdit)
    mes = decodeRotor(rotor3,message)
    print(mes)
    mes = decodeRotor(rotor2,mes)
    print(mes)
    mes = decodeRotor(rotor1,mes)
    print(mes)
    mes = cesarDecode(mes,nombre)
    print(mes)
    return ''.join(mes)




alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
listRotor1 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
listRotor2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
listRotor3 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")

message = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
decodeMessage = "KFD"
nombre = 4
messageEncoder = encode(listRotor1,listRotor2,listRotor3,message,nombre)
#decodeMessage = messageEncoder
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
messageDecoder = decode(listRotor1,listRotor2,listRotor3,decodeMessage,nombre)


print("Message de base:" + message)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Message encoder: " + messageEncoder)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Message decoder: " + messageDecoder)

