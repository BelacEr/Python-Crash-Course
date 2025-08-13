pets = {    # dictionary with the pets' name and its information
    'Jack': {
        'animal': 'cat',
        'owner': 'caleb',
        },

    'Luna': {
        'animal': 'dog',
        'owner': 'isabel',
        },

    'Milo': {
        'animal': 'dog',
        'owner': 'camila'
        },

    }

for pet, pet_info in pets.items():  # for loop to get the pets' name and its information
    print(f"\nPet's name: {pet}")
    animal = f"{pet_info['animal']}"
    owner = f"{pet_info['owner']}"    
    
    print(f"Animal: {animal.title()}")
    print(f"Owner: {owner.title()}")

