from city_function import get_formatted_city_country

def test_city_country():
    """Do city and country names like 'Chile, Santiago' work?"""
    formatted_city_country = get_formatted_city_country('Chile', 'Santiago')
    assert formatted_city_country == 'Chile, Santiago'
