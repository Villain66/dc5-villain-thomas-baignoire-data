class Entreprise:
    def __init__(self, name, nb_clients, client_revenue):
        self.name = name
        self.nb_clients = nb_clients
        self.client_revenue = client_revenue

entreprise1 = Entreprise("apple", 500000, 200)

function = entreprise1.nb_clients * entreprise1.client_revenue

print(function)