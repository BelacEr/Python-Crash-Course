favorite_places = {     # dictionary with people's name and their favorite places
    
    'Isabela Reyes': (
        'Museo Frida Kahlo',
        'Parque México (en la Condesa)',
        'Librería El Péndulo',
        ),

    'Camila Navarro': (
        'Teatro Degollado',
        'Cafetería PalReal',
        'Boque Los Colomos',
        ),

    'Renata Cruz': (
        'Parque Fundidora',
        'Mirador del Obispado',
        'Museo MARCO (Museo de Arte Contemporáneo)',
        ),

        }

for name, place in favorite_places.items(): # for loop to get their names and favorite places
    print(f"\n{name.title()}'s favorite places:")
    print(", ".join(place))     # print the list
