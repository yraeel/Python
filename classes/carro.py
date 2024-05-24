class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #kilometragem do carro definido como 0 como valor padrão
    

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    # funcao para verificar a kilometragem do veiculo
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    #funcao para atualizar a kilometragem do veiculo
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode reduzir a kilometragem do veiculo!")
    

    def increment_odometer(self,miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)

my_new_car.increment_odometer(200)
my_new_car.read_odometer()