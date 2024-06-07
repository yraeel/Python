

arquivo = "Livro_Python/arquivos/lista_de_convidados.txt"


# -----------CODIGO ABAIXO ESCREVE COISAS NO ARQUIVO
"""
# while True:
#     nome = input("digite seu nome: ")
#     if nome == 's':
#         break
    
#     print(f"Saudações: {nome}")  


#     with open(arquivo, 'a') as file_object:
#         file_object.write(f'{nome}\n')

"""
        



# -------- CODIGO ABAIXO POSSUI UMA FUNCAO QUE O USUARIO DIGITA O NOME DO CONVIDADO
# E VERIFICA QUANTAS VEZES ELE REPETE
# POSSUI TBM UM TRY EXCEPT ONDE VERIFICA SE O ARQUIVO EXISTE OU NÃO
# CRIAR UMA FUNCAO DEPOIS PARA INSERIR CONVIDADOS NA LISTA

def contagem_convidados(arquivo):
    while True:
            
        try:
            with open(arquivo) as f_obj:
                content = f_obj.read()
                nome = input("Digite o nome do convidado: ")
                
        
        except FileExistsError:
            msg = "Arquivo não existe."
            print(msg)
        
        else:
            count_convidado = content.lower().count(nome)
            print(count_convidado)

contagem_convidados(arquivo)