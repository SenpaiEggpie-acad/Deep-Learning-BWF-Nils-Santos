favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

names = ['jen','sarah','julia','ken', 'harold', 'bob']

for name in names:
    if name not in favorite_languages.keys():
        print("Hello {fname}, we invite you to take our languages poll.".format(fname=name.title()))

    else:
        print("Thank you for answering our poll.")