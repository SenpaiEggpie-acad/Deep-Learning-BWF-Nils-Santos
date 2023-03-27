#Made by Nils Santos
pet1 = {'name' : 'Peppa',
         'animal':'pig',
         'owner': 'George'}

pet2 = {'name': 'Leonardo',
        'animal':'turtle',
        'owner': 'April'}

pet3 = {'name': 'Boots',
        'animal':'monkey',
        'owner': 'Dora'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\n")
    for key, value in pet.items():
        print(key + " - " + value)