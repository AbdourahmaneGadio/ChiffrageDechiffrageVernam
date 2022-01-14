# coding:utf-8

def cleK(message, cle):
    """
    Fonction qui chiffre un message avec
    une clé K qui appartient à B^p (p € N*)

    ENTREE : Une chaîne de caractères
    SORTIE : Une chaîne de 0 et de 1
    """

    codeChiffre = []
    indiceCode = 0

    # Chiffrement
    for lettre in message:

        if lettre == cle[indiceCode]: # Si les chiffres sont égaux
            codeChiffre.append("0")
        else:
            codeChiffre.append("1")

        indiceCode+=1

        if indiceCode == len(cle): # Si x ème lettre, on remet à 0
            indiceCode = 0     

    return codeChiffre


message = input("Entrez un message : ")
message = str(message)

cle = input("Entrez une clé : ")
cle = str(cle)

print "Clé chiffré", cleK(message, cle)
cleChiffre = cleK(message, cle)

print "Clé déchiffré", cleK(cleChiffre, cle)


