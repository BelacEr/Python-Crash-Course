guests = ['Ana', 'Gabo', 'Miguel', 'Maressa', 'Arix', 'Monika']

def dinner(guests_list):    # function to call each item in the list
    for guest in guests_list:  
        print(f'I would like to have a dinner with you, {guest}.')    

def pop_list(remove_list):
    for guest in remove_list[2:8]:  # Get guests at positions 2 to 8
        print(f"Sorry {guest} for not being able to invite you to dinner.")
    del remove_list[2:8]

def still_invited(invited):
    for guest in invited:  # Iterate through remaining guests
        print(f"You're still invited to the dinner, {guest}.")

dinner(guests)  # call dinner function

print('\tI found a bigger table.')
# add new friends
guests.insert(3, 'Ariel')
guests.append('Hypervisor')

dinner(guests)  # call dinner function with changed list

print('\n\tA problem arose, I can only invite two people.\n')

pop_list(guests)
print('\n')
still_invited(guests)

del guests[0:2]
print(guests)