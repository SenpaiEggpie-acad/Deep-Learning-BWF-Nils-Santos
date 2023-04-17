#Made by Nils Santos
magician_list = ['Magic Man', 'Dr. Fate', 'Dr. Strange', 'Mr. M',
                 'Zatana']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    temp_list = []
    for magician in magicians:
        magician = ("the Great " + magician)
        temp_list.append(magician)
    magicians = temp_list.copy()
    return magicians

make_great(magician_list)
show_magicians(magician_list)
