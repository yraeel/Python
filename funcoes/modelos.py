

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design)
        
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("The following models have been printed: ")

    for completed_model in completed_models:
        print(completed_model)




print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
# função chamada show_magicians() que exiba o nome de cada mágico da
# lista.

# 8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
# Exercício 8.9. Escreva uma função chamada make_great() que modifique a
# lista de mágicos acrescentando a expressão o Grande ao nome de cada
# mágico. Chame show_magicians() para ver se a lista foi realmente modificada.

# 8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
# Chame a função make_great() com uma cópia da lista de nomes de mágicos.
# Como a lista original não será alterada, devolva a nova lista e armazene-a em
# uma lista separada. Chame show_magicians() com cada lista para mostrar que
# você tem uma lista de nomes originais e uma lista com a expressão o Grande
# adicionada ao nome de cada mágico.
