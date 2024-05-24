class Dog():
    def __init__(self, name, age): # inicializa os atributos name e age
        self.name = name
        self.age = age
    
    def sit(self): #simula a ação de sentar
        print(self.name.title() + " está sentado.")
    
    def roll_over(self): # simula a ação de rolar
        print(self.name.title() + " está rolando.")



my_dogo = Dog('jake', 12)

print("My dog's name is " + my_dogo.name.title() + ".")

my_dogo.sit()
my_dogo.roll_over()