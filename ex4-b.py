def factoriel(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factoriel(number - 1)
    
test_1 = 0
test_2 = 4
test_3 = 12

resultat_1 = factoriel(test_1)
resultat_2 = factoriel(test_2)
resultat_3 = factoriel(test_3)

print(f"Le factoriel de {test_1} est {resultat_1}")
print(f"Le factoriel de {test_2} est {resultat_2}")
print(f"Le factoriel de {test_3} est {resultat_3}")