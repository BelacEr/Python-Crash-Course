from city_population_function import get_formatted_city_country_population as get_formatted

def test_city_country():
    """Do names like 'Santiago, Chile' work?"""
    formatted_cities = get_formatted('santiago', 'chile')
    assert formatted_cities == 'Santiago, Chile'

def test_city_country_population():
    """Do names and information about the population like 'Santiago, Chile - population 5000000' work?"""
    formatted_cities_population = get_formatted('santiago', 'chile', population=5_000_000)
    assert formatted_cities_population == 'Santiago, Chile - population 5000000'
