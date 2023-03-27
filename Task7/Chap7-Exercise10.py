#Made by Nils Santos
places = []
votes_dict={}
place = ""

while place != 'quit':
    place = str(input('If you could visit one place in the world, where would you go?'))
    
    if place == 'quit':
        break

    if place.title() in votes_dict.keys():
        votes_dict[place.title()] += 1
    else:
        votes_dict[place.title()] = 1
    

print("Poll results: \n")
for place, votes in votes_dict.items():
    print(place + ": " + str(votes))
