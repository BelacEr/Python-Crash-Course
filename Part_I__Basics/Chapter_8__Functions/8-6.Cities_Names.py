def city_country(city, country):
    string_format = (f"\n{city}, {country}.")
    return string_format.title()

formatted_string = city_country("santiago", "chile")
print(formatted_string)

formatted_string = city_country("Mexico City", "Mexico")
print(formatted_string)

formatted_string = city_country("Washington D.C.", "United States")
print(formatted_string)
