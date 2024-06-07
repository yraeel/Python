import json

filename = 'usuario.json'



lista_usuarios = []


def add_user():
    """
    
    Função que adiciona um novo usuario a lista de usuarios.
    
    """
    name = input("Digite nome e sobrenome: ")
    email = input("Digite seu email: ")
    idade = int(input("Digite sua idade: "))
    lista_usuarios.append({'name' : name, 'email': email, 'idade': idade})





def salvar_user():
    
    """
    Função para salvar a lista de usuários no arquivo JSON.
    Lê os usuários existentes do arquivo, adiciona novos usuários e salva a lista atualizada.
    """
    
    try:
        # tenta ler os usuarios existentes no arquivo
        with open(filename, 'r') as file_obj:
            existing_users = json.load(file_obj)

    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio, inicializa uma lista vazia
        existing_users = []

    # Adicionar novos usuários à lista existente
    existing_users.extend(lista_usuarios)
    
    # Escrever a lista atualizada de volta no arquivo
    with open(filename, 'w') as file_obj:
        json.dump(existing_users, file_obj)





def verificando():

    """
    Função para verificar e imprimir os usuários armazenados no arquivo JSON.
    """

    try:
         # Tentar ler os usuários do arquivo
        with open(filename, 'r') as file_obj:
            lista_usuarios = json.load(file_obj)
            
            # Imprimir cada usuário na lista
            for usuarios in lista_usuarios:
                print(usuarios)

    except FileNotFoundError:
        return 'Nenhum usuario encontrado.'






verificando()