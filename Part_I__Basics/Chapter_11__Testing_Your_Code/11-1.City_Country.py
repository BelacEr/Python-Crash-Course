from city_function import get_formatted_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me the name of your city: ")
    if city == 'q':
        break
    country = input('\nPlease give me the name of you country: ')
    if country == 'q':
        break

    formatted_city_country = get_formatted_city_country(city, country)
    print(f"\tNeatly formatted city country: {formatted_city_country}.")
