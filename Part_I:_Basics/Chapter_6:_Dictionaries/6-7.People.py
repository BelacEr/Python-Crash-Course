people = {

    'Isabela': {
        'first': 'Isabela',
        'last': 'Reyes',
        'age': 18,
        'city': 'Mexico City',
        },

    'Camila': {
        'first': 'Camila',
        'last': 'Navarro',
        'age': 20,
        'city': 'Guadalajara',
        },

    'Renata': {
        'first': 'Renata',
        'last': 'Cruz',
        'age': 19,
        'city': 'Monterrey',
        },

    }

for person, information in people.items():
    print(f"\n{person.title()} information:")
    full_name = f"{information['first'].title()} {information['last'].title()}"
    age = f"{information['age']}"
    city = f"{information['city'].title()}"

    print(f"\tFull name: {full_name}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city}")


