def describe_city(city, country='Mexico'):
    print(f"\n{city.title()} is in {(country.title())}.")

describe_city('Mexico City')
describe_city('Monterrey')
describe_city('Washington D.C.', 'United States')
