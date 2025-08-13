guests = ['Ana', 'Gabo', 'Miguel', 'Maressa', 'Arix', 'Monika']

def dinner(guests_list):
    for i in range(len(guests_list)):
        print(f'I would like to have a dinner with you {guests_list[i]}.')    

dinner(guests)  

print('I found a bigger table.')
# add new friends
guests.insert(3, 'Ariel')
guests.append('Hypervisor')

dinner(guests)  # call dinner function with changed list

print('\nThe number of people I\'m inviting to dinner is:', len(guests))
