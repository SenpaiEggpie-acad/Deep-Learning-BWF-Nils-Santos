#Made by Nils Santos

text = 'hotdog'
print("Is text == 'hotdog'? I predict True.")
print(text == 'hotdog')

text = 'burger'
print("\nIs text == 'fries'? I predict False.")
print(text == 'fries')

text = 'abc'
print("\nIs text in lowercase? I predict True.")
print(text == text.lower())

text = 'ABC'
print("\nIs text in lowercase? I predict False.")
print(text == text.lower())

number = 1
print("\nIs number == 1? I predict True.")
print(number == 1)

number = 1
print("\nIs number == 2? I predict False.")
print(number == 2)

number = 10
print("\nIs number > 2? I predict True.")
print(number > 2)

number = 10
print("\nIs number < 2? I predict False.")
print(number < 2)

the_list = [1,2,3,4,5,6,7,8]
print("\nIs 2 in the list? I predict True.")
print(the_list.count(2) > 0)

the_list = [1,2,3,4,5,6,7,8]
print("\nIs 10 in the list? I predict False.")
print(the_list.count(10) > 0)