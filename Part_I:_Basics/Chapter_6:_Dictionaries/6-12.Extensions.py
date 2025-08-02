usernames = {

    'isabel': {
        'first': 'Isabela',
        'last': 'Reyes',
        'age': 18,
        'city': 'Mexico City',
        },

    'cami': {
        'first': 'Camila',
        'last': 'Navarro',
        'age': 19,
        'city': 'Guadalajara',
        },

    'rena': {
        'first': 'Renata',
        'last': 'Cruz',
        'age': 20,
        'city': 'Monterrey',
        },
    }

for username, username_info in usernames.items():
    print(f"{username.title()} username information".center(40, '='))

    full_name = f"{username_info['first']} {username_info['last']}"
    age = f"{username_info['age']}"
    city = f"{username_info['city']}"

    print(f"\nFull name: {full_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}\n")

# print(f"{information['name']} {information['last_name']} is {information['age']} years old and lives in {information['city']}.")
