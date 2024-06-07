
filename = "Livro_Python/arquivos/arquivo.txt"


# with open(filename) as file_object:
#     lines = file_object.readlines()
#     for i in range(3):
#         print(i+1)
#         for line in lines:
#             print(line)


# # abrindo e lendo o conteudo do arquivo
# with open(filename) as file_object:
#     lines = file_object.readlines()

# # substituindo a frase do arquivo 'tenho 23 anos' por 'eu sou um programador python'
# # aparentemente não alterou o arquivo original
# for line in lines:
#     linha = line.replace('tenho 23 anos', 'eu sou um programador python')
#     print(linha)






# outro_arquivo = "Livro_Python/arquivos/teste.txt"

# ----------- ABRINDO O ARQUIVO PARA ESCRITA-----------------
# ADENDO: com o modo W  -escrita, o arquivo não salvará os dados anteriores ou futuros
# ou seja, cada vez que vc acrescentar algo, o texto anterior irá apagar

# with open(outro_arquivo, 'w') as file_object: # abrindo o arquivo com modo de escrita utilizando o w
#     file_object.write('Eu sou um programador.\n')
#     file_object.write('Israel Machado.\n')


# ---------------- ABRINDO ARQUIVO COM MODO CONCATENAÇÃO----------------
# usando o modo concatenação, você consegue adicionar novas linhas no arquivo
# with open(outro_arquivo, 'a') as file_object:
#     while True:
#         nome = input("digite seu nome: ")
#         file_object.write(nome)
    

