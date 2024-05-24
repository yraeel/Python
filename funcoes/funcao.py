# def describe_pet(animal = 'dog', nome):
#     print(f'eu tenho um {animal} e o nome é {nome}')


# describe_pet('hamster', 'rochelle')



# toda vez que for passar um parametro que tenha um valor padrão
# o parametro com o valor padrão deve vir DEPOIS de todos os parametros
# que nao possuem valor, pois ira bugar ou dar erro, exemplo acima e abaixo.

# def describe_pet(nome, animal ='cachorro'):
#     print(f'eu tenho um {animal} e o nome é {nome}')


# describe_pet('rochelle')



# argumentos posicionais, onde cada vc precisa relacionar a ordem do argumento
# para adicionar o valor
# tamanho : m
# texto : 'halo world
# atenção pois pode haver uma troca se não verificar a posição dos argumentos

# def make_shirt(tamanho, texto):
#     print(f'Camiseta tamanho: {tamanho}\nTexto: {texto}')

# make_shirt('M', 'Hallo World')


# def describe_city(cidade, pais):
#     print(f'{cidade} está localizado(a) em {pais}')


# describe_city('Rio das ostras', 'Rio de Janeiro')




# def build_person(nome, sobrenome):
#     person = {'primeiro_nome': nome,
#               'ultimo_nome' : sobrenome,}
    
#     return person

# pessoa = build_person('Israel', 'Machado')
# print(pessoa)



# def city_country(cidade, pais):
#     result = cidade + ', ' + pais
#     print(result)

# city_country('Santiago', "Chile")
# city_country('Sidney', "Australia")
# city_country('Rio das Ostras', "Brasil")




#argumento 'faixa' é um argumento opcional
#caso o usuario queira colocar, ele será incluido, argumentos opcionais devem ficar por ultimo

def make_album(nome_artista, titulo, faixa=''):

# condição para argumento opcional
    if faixa:
        album = {'artista': nome_artista,
              'musica' : titulo,
              'faixas': faixa}
        
    else:
        album = {'artista': nome_artista,
                'musica' : titulo,}
        
    return album

musica = make_album('Israel', 'Jardim do eden','5')
outra_musica = make_album('alicia', 'pais das maravilhas')
print(musica)
print(outra_musica)