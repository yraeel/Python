def make_pizza(size, *toppings):
    print(f'Pizza tamanho {size}')
    for topping in toppings:
        print(' - ' + topping)

make_pizza(16, 'pepperoni', 'queijo','oregano')
make_pizza(12, 'peru', 'bacon')

