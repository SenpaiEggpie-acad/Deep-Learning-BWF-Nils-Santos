#Made by Nils Santos
favorite_places = {'Charles': ['Intramuros'],
                   'Stephen': ['Rizal, Poblacion'],
                   'Trevor': ['Manila Bay, Taft, Ermita']}

for person, fave_places in favorite_places.items():
    print("\n"+ person + "'s favorite place/s are:")
    for place in fave_places:
        print(place)