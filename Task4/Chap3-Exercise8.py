#Made by Nils Santos
places = ['New York', 'Seoul', 'Maldives', 'Sao Paulo', 'Busan']
print("Original arrangement: {list}".format(list=places))
print("Alphabetical arrangement: {list}".format(list=sorted(places)))
print("Reverse alphabetical arrangement: {list}".format(list=sorted(places, reverse=True)))
print("Original list is still untouched: {list}".format(list=places))
places.reverse()
print("Original list is now reversed: {list}".format(list=places))
places.reverse()
print("Reversed list reverted back to original: {list}".format(list=places))
places.sort()
print("Original list in alphabetical order: {list}".format(list=places))
places.sort(reverse=True)
print("Original list in reverse alphabetical order: {list}".format(list=places))
