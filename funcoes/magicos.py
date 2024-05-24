# def show_magicians(names):
#     for name in names:
#         msg = 'Olá: ' + name.title()
#         print(msg)

# usernames = ['israel', 'alicia']
# wizards = usernames

# show_magicians(usernames)




magicos = ['israel', 'alicia']
wizards = []

def show_magicians(magicos):
    for magico in magicos:
        print(f'Olá {magico}')

show_magicians(magicos)

outra_lista = magicos.pop()

wizards.append(outra_lista)

for wizard in wizards:
    print(f'O grande  {wizard}')


