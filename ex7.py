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

def depenses(clients):
    total = 0
    for client in clients:
        total += client["montant_depense"]
    return round(total,2)

montant_total_depense = depenses(clients)

print(f"Le montant total dépensé par tous les clients vaut : {montant_total_depense}€")