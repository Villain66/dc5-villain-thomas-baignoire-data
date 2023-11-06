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

nombre_mots = 0
precedent_alphanum = False
precedent_ponctuation = False

for caractere in chaine_originale:
    if ('a' <= caractere <= 'z') or ('A' <= caractere <= 'Z') or ('0' <= caractere <= '9') or caractere in "àâäéèêëïîôöùûüç":
        if not precedent_alphanum:
            nombre_mots += 1
        precedent_alphanum = True
        precedent_ponctuation = False 
    else:
        if caractere in "'-!.?,":
            if not precedent_ponctuation:
                nombre_mots += 1
            precedent_ponctuation = True
        else:
            precedent_ponctuation = False
        precedent_alphanum = False


print(f"Phrase en majuscules : {''.join(chaine_convertie_majuscule)}")
print(f"Phrase en minuscules : {''.join(chaine_convertie_minuscule)}")
print(f"Nombre de mots dans la phrase : {nombre_mots}")