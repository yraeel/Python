from dataclasses import dataclass


# primeira forma de criar uma classe
"""
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def exibir(self):
        print(self.nome, self.idade)
        
        
    
israel = Pessoa('israel', '23 anos')
alicia = Pessoa('alicia', '23 anos')

# para exibir as informaçoes da pessoa que foi criada:

print(israel.nome, israel.idade)
# é necessario chamar o nome da variavel seguido do seu parametro, como acima
# ou utilizar uma função, como é a função 'def exibir()' 
# que da um print nos atributos da variavel que for atribuida a classe

alicia.exibir()

"""



# segunda forma de criar uma classe

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str

    def exibir(self): # metodo exibir da classe
        print(f'Nome: {self.nome} \nIdade: {self.idade}\nEmail: {self.email}')


israel = Pessoa('israel', 23, 'israelmachado@real.com')

israel.exibir()

