#Made by Nils Santos

prog_words = {'append':"add something to a list",
              'lower': "turn a string to lowercase",
              'title': "turn a string to title case",
              'del': "remove",
              'if-elif': "a chain of conditional statements using if and elif"}

for key, value, in prog_words.items():
    print(key + " - " + value)