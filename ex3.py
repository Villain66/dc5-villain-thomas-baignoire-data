cout = float(input("Veuillez entrer le coût de la campagne en euros : "))

revenu = float(input("Veuillez entrer le revenu généré par la campagne en euros: "))

if revenu > cout:
    montant_rentabilite = revenu - cout
    print(f"Bravo ! La campagne a été rentable de {montant_rentabilite}€")
elif revenu == cout:
    print("La campagne a atteint son seuil de rentabilité.")
else:
    montant_non_rentabilite = cout - revenu
    print(f"Oups ! La campagne n'a pas été rentable de {montant_non_rentabilite}€")