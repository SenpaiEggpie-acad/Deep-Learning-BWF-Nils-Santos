#Made by Nils Santos
rivers = {'Nile': 'Egypt',
          'Amazon': 'South America',
          'Yangtze': 'China'}
for key, value, in rivers.items():
    print(key + " runs through " + value)

print('\nThe rivers are:')
for key in rivers.keys():
    print(key)

print("\nThe countries are:")
for value in rivers.values():
    print(value)