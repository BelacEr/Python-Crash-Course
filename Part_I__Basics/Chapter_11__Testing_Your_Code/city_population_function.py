def get_formatted_city_country_population(city, country, population=''):
    """Get the name of the city and country and print it on the "City, Country" form."""
    if population:
        formatted_city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country
