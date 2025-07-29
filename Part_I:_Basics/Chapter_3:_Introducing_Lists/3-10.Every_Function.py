languages = ['english', 'spanish', 'portuguese', 'french']

print('The list in its original order: ')
print(languages)

print('\nThe list in alphabetical order (temporal order): ') 
print(sorted(languages))     # temporal order

print('\nThe list in its original order (again): ')
print(languages)

print('\nThe list in reverse-alphabetical order (temporal order): ')
print(sorted(languages, reverse=True))  # temporal order

print('\nThe lits in its original order (again): ')
print(languages)

languages.reverse()
print('\nThe list in its reverse order: ')
print(languages)

languages.reverse()
print('\nThe lits in its original order: ')
print(languages, '\n')

