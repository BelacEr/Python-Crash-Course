favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
        }

people = ('jen', 'gabo', 'ana', 'sarah', 'isabela', 'monika', 'phill')

for name in people:
    if name not in favorite_languages:
        print(f'{name.title()}, please take our poll!')
    else:
        print(f'{name.title()}, thank you for taking the poll.')

