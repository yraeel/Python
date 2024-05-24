lista = ['nilson', 'cris', 'julia']

removido = lista.pop(0)
alterado = lista.insert(0, 'alicia')
lista.insert(0, 'jake')
lista.insert(2, 'lola')
lista.append('ciça')

removido1 =lista.pop(5)
removido2 = lista.pop(4)
removido3 =lista.pop(3)
removido4 =lista.pop(2)



print(removido1 + ' desculpe')
print(removido2 + ' desculpe')
print(removido3 + ' desculpe')
print(removido4 + ' desculpe')


print("Voce " + lista[0] + ' ainda esta convidado')

print("Voce " + lista[1] + ' ainda esta convidado')

print( removido + ' não poderá comparecer')

del lista[0]
del lista[0]

print(lista)