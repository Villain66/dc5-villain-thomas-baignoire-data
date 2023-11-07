import random
import string

def generation_email():
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(7)) + "@gmail.com"

clients = [
    {
        "nom": f"Client{i}",
        "email": generation_email(),
        "montant_depense": round(random.uniform(10.0, 200.0), 2)
    }
    for i in range(1, 51)  # Permet de générer 50 entrées
]

# Permet d'afficher le dicitionnaire avec condition :
for client in clients:
     if client["montant_depense"] > 100:
        print(f"Nom: {client['nom']}, Email: {client['email']}, Montant dépensé: {client['montant_depense']}€")