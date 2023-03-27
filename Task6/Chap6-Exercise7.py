person1 = {'first_name': 'Johnny',
          'last_name': 'Depp',
          'city': 'New York'}

person2 = {'first_name': 'Amber',
          'last_name': 'Heard',
          'city': 'Seattle'}

person3 = {'first_name': 'Elon',
          'last_name': ' Musk',
          'city': 'Boston'}

person_list = [person1, person2, person3]

for person in person_list:
    for key, value in person.items():
        print(key + ": " + value )
    
    print("\n")