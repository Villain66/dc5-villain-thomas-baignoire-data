liste = [2, 6, 6, 7, -9, -3, 6, 2, 11, 60]
if liste == []: 
    print("Liste vide")
else :
    minimum = liste[0]
    maximum = liste[0]
    somme = 0
    diviseur = 0

    for number in liste:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    for number in liste:
        somme += number
        diviseur += 1

    moyenne = somme / diviseur if diviseur != 0 else 0

    print("Minimum : ", minimum)
    print("Maximum : ", maximum)
    print("Moyenne : ", moyenne)