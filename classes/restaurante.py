class Restaurante():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.server_clients = 0
       
    

    def describe_restaurant(self):
        print(f'Restaurante: {self.name.title()}')
        print(f'Tipo: {self.cuisine.title()}')
    

    def open_restaurant(self):
        print(f'O {self.name.title()} está aberto.')

    
    def set_number_served(self):
        print("O restaurante atendeu: " + str(self.server_clients) + " clientes.")

    def increment_number_served(self, clientes):
        self.server_clients += clientes
   

restaurante = Restaurante('Burguer burguers', 'artesanal')


restaurante.describe_restaurant()
restaurante.open_restaurant()
restaurante.increment_number_served(100)
restaurante.set_number_served()


