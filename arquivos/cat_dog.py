


filename = "Livro_Python/arquivos/cat.txt"

# nome = input("Digite: ")
# with open(filename, 'a') as f_obj:
#     f_obj.write(f'{nome}\n')


try:
    with open(filename) as f_obj:    
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg = 'arquivo n existe'
    print(msg)