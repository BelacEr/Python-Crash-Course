rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze':'china',
        }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")


print(f"\nThe rivers included in the dictionary:")
for river in rivers:
    print('\t', river.title())


print(f"\nThe name of each country included in the dictionary:")
for country in rivers.values():
    print('\t', country.title())


