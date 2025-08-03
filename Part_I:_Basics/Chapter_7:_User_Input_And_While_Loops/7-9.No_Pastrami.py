sandwich_orders = ['Pastrami', 'Club', 'Cuban', 'Egg salad', 'Chicken', 'Pastrami',
                   'Monte Cristo', 'Ham and cheese', 'Pastrami',]
finished_sandwiches = []



while sandwich_orders:
    
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
    

    current_sandwich = sandwich_orders.pop()        # get the last item of the list

    print(f"\nI made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)    # move it to the list of finished sandwiches

# print each sandwich that was made
print("\n---Each sandwich that was made---\n") 
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich.")
