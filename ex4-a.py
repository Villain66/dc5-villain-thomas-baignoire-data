def conversion_pourcent(ctr):
    pourcentage = ctr * 100
    return pourcentage

ctr_test_1 = 0.34
ctr_test_2 = 0.51
ctr_test_3 = 0.66

resultat_1 = conversion_pourcent(ctr_test_1)
resultat_2 = conversion_pourcent(ctr_test_2)
resultat_3 = conversion_pourcent(ctr_test_3)

print(f"Le CTR1 est de {resultat_1}%")
print(f"Le CTR2 est de  {resultat_2}%")
print(f"Le CTR3 est de {resultat_3}%")