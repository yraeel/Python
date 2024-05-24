


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


while True:
    nome_do_artista = input("Digite o nome do artista ou 'Q' para sair: ")

    if nome_do_artista == 'q':
        break

    nome_da_musica = input("Digite o nome da musica ou 'Q' para sair: ")

    if nome_da_musica == 'q':
        break

    minutos = input("Digite os minutos da musica ou 'Q' para sair ou ENTER para continuar: ")

    if minutos == 'q':
        break
    else:
        album_de_musica = make_album(nome_do_artista, nome_da_musica, minutos)
        print(album_de_musica)



    






# def get_formatted_name(first_name, last_name):
#     full = first_name + ' ' + last_name
#     return full.title()

# while True:
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name) 

#     print(formatted_name)

























