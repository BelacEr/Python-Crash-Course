guests = ['Ana', 'Gabo', 'Miguel']

for i in range(len(guests)):
    print(f'I would like to have a dinner with you {guests[i]}.')    
    
cant_come = guests.pop()

print(f"\n\t{cant_come} will not come.\n")

guests.append('Maressa')

for i in range(len(guests)):
    print(f"I would like to have a dinner with you {guests[i]}.")