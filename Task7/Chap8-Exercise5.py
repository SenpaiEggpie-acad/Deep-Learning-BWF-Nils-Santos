#Made by Nils Santos

def describe_city(city, country = "Korea"):
    print("{city} is in {country}".format(city=city.title(),country=country.title()))

describe_city('Busan')
describe_city('Seoul')
describe_city('Manila', 'Philippines')