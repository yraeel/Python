from argumentos import modelos


"""
8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez.
"""
# def make_sand(*itens):
#     print('Sanduiche de: ')
#     for item in itens:
#         print(f' - ' + item)

# make_sand('presunto','queijo','peito de peru', 'alface', 'tomate')
# make_sand('queijo parmesão','peito de peru', 'alface', 'tomate')
# make_sand('presunto','peito de peru')


"""


8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam.
"""

# def build_profile(first, last, **user_info):
#     """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
#     profile = {}

#     profile['first_name'] = first
#     profile['last_name'] = last

#     for key, value in user_info.items():
#         profile[key] = value

#     return profile 
        
# user_profile = build_profile('Israel', 'Machado', location = 'rio de janeiro', field = 'developer', altura = '1.71')
    
# print(user_profile)

"""
8.14 – Carros: Escreva uma função que armazene informações sobre um carro
em um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser
aceito. Chame a função com as informações necessárias e dois outros pares
nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
que todas as informações foram armazenadas corretamente.

"""


def make_car(fabricante, modelo, **car_info):
    
    carro = {}

    carro['fabricante'] = fabricante
    carro['modelo'] = modelo

    for key, value in car_info.items():
        carro[key] = value
    
    return carro

carro_profile = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(carro_profile)



