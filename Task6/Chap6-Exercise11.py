cities = {'Seoul': {'country': 'Korea',
                    'population': '9988000',
                    'fact': 'Seoul is highly urbanized and has little green space'},

          'Manila': {'country': 'Philippines',
                     'population': '1780000',
                     'fact': 'It is the capital of the Philippines.'},

          'New York': {'country': 'USA',
                     'population': '8468000',
                     'fact': 'It is the most linguistically diverse city in the world.'}
}

for city, info_dict in cities.items():
    print(city)
    for category, info in info_dict.items():
        print(category + ": " + info)
    print("\n")
          