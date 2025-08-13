cities = {

    'kyoto': {
        'country': 'japan',
        'population': '~1.45 million',
        'fact': 'Kyoto was the capital of Japan for over 1,000 years '
        'and is home to more than 1,600 Buddhist temples.',
        },

    'medellín': {
        'country': 'colombia',
        'population': '~2.5 million',
        'fact': 'Once considered one of the most dangerous cities '
        'Medellín is now known for its innovation and public '
        'transportation systems, including the first metro in Colombia '
        'and cable cars serving poor hillside neighborhoods.',
        },
        
    'lisbol': {
        'country': 'portugal',
        'population': '~545,000',
        'fact': 'Lisbon is older than Rome and is one of the oldest '
        'cities in Western Europe — it even predates London, Paris, and Madrid.',
        },

    }

# for loop to print the name of the country and all of the information
for city, city_info in cities.items():  
    print(f"\n{city.title()}'s information:")

    # city information variables
    country = f"{city_info['country']}"         
    population = f"{city_info['population']}"    
    fact = f"{city_info['fact']}"

    print(f"\tCountry: {country.title()}")        # country
    print(f"\tPopulation: {population.capitalize()}")  # popoulation
    print(f"\tFact: {fact}")              # fact
