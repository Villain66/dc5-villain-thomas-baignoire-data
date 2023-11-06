def convertir_en_majuscule(chaine):
    chaine_majuscule = []
    for caractere in chaine:
        valeur_ascii = ord(caractere)
        if 97 <= valeur_ascii <= 122:
            caractere_majuscule = chr(valeur_ascii - 32)
        else:
            caractere_majuscule = caractere
        chaine_majuscule.append(caractere_majuscule)
    return chaine_majuscule

def convertir_en_minuscule(chaine):
    chaine_minuscule = []
    for caractere in chaine:
        valeur_ascii = ord(caractere)
        if 65 <= valeur_ascii <= 90:
            caractere_minuscule = chr(valeur_ascii + 32)
        else:
            caractere_minuscule = caractere
        chaine_minuscule.append(caractere_minuscule)
    return chaine_minuscule

chaine_originale = input("Tapez une phrase : ")
chaine_convertie_majuscule = convertir_en_majuscule(chaine_originale)
chaine_convertie_minuscule = convertir_en_minuscule(chaine_originale)

print(f"Phrase en majuscules : {''.join(chaine_convertie_majuscule)}")
print(f"Phrase en minuscules : {''.join(chaine_convertie_minuscule)}")
print(f"Nombre de caractères : {len(chaine_originale)}")
