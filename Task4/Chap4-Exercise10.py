#Made by Nils Santos
numbers = list(range(1,21))
print("First three items are: " + str(numbers[:3]))
print("Middle three items: " +str(numbers[int(len(numbers)/2)-2:int(len(numbers)/2)+1]))
print("Last three items: " + str(numbers[-3:]))