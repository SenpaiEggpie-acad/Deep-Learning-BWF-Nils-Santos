#Made by Nils Santos
fav_numbers = {'Nils':[1,3],
              'Brix':[10, 23, 65],
              'Kerth':[21, 22, 23],
              'John':[1000, 21412, 513221, 12312],
              'Abby':[99, 456, 4131231, 123123]}
for name, numbers in fav_numbers.items():
    print(name + ": ")
    for number in numbers:
        print(number)
    
    print("\n")