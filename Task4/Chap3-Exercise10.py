#Made by Nils Santos
phone_brands = ['HTC', 'Vivo', 'Google', 'Apple', 'Samsung']
print("Number of brands: " + str(len(phone_brands)))

#Pop, insert, append
phone_brands.insert(0,'Lenovo')
phone_brands.append('Infinix')
print(phone_brands.pop())

#Sorting
print("Original arrangement: {list}".format(list=phone_brands))
print("Alphabetical arrangement: {list}".format(list=sorted(phone_brands)))
print("Reverse alphabetical arrangement: {list}".format(list=sorted(phone_brands, reverse=True)))
print("Original list is still untouched: {list}".format(list=phone_brands))
phone_brands.reverse()
print("Original list is now reversed: {list}".format(list=phone_brands))
phone_brands.reverse()
print("Reversed list reverted back to original: {list}".format(list=phone_brands))
phone_brands.sort()
print("Original list in alphabetical order: {list}".format(list=phone_brands))
phone_brands.sort(reverse=True)
print("Original list in reverse alphabetical order: {list}".format(list=phone_brands))

#Deleting list
del phone_brands[:]
print("Phone Brands: " + str(phone_brands))
