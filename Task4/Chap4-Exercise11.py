#Made by Nils Santos
my_pizza = ['Pepperoni pizza', '4-Cheese pizza', 'Hawaiian pizza']

friend_pizzas = my_pizza[:]
my_pizza.append('BBQ pizza')
friend_pizzas.append('Meat Overload pizza')

print('My favorite pizzas are:\n')
for pizza in my_pizza:
    print(pizza)

print('\n')
print("My friend's favorite pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza)
