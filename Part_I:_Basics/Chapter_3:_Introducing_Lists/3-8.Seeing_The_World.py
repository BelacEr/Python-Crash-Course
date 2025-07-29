locations = ['Spain', 'Argentina', 'United States', 'Finland', 'Norway']

print('The list in its original order: ')
print(locations)

print('\nThe list in alphabetical order: ')
print(sorted(locations))

print('\nThe list in its original order (again): ')
print(locations)

print('\nThe list in reverse-alphabetical order: ')
print(sorted(locations, reverse=True))

print('\nThe lis in its original order (again): ')
print(locations)

locations.reverse()     # reverse the order of the list

print('\nThe list in reverse order: ')
print(locations)

locations.reverse()     # reverse the order of the list (in its original order)

print('\nThe list in its original order (again): ')
print(locations)

locations.sort()        # sort the list in alphabetical order

print("\nThe list in alphabetical order: ")
print(locations)

locations.sort(reverse=True)    # sort the list in reverse-alphabetical order

print('\nThe list in reverse-alphabetical order: ')
print(locations, '\n')
