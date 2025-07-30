def print_loop(pizzas):
    for pizza in pizzas:
        print(pizza)

pizzas = ['Pepperoni', 'Hawaiian', 'Four Cheese']

for pizza in pizzas:
    print(f"I like {pizza.lower()} pizza.")
print('\nI really love pizza!')

friend_pizzas = pizzas[:]

pizzas.append("Meat Lover’s")
friend_pizzas.append('BBQ Chicken')



print('\nMy favorite pizzas are: \n')
print_loop(pizzas)

print("\nMy friend's favorite pizzas are: \n")
print_loop(friend_pizzas)
