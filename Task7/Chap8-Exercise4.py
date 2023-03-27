#Made by Nils Santos

def make_shirt(size='Large', text='I love Python'):
    print("The size is {size}. The text is {text}.".format(size=size,text=text))

make_shirt() #Large size and default text
make_shirt(size = 'Medium') #Medium size and default text
make_shirt(size = 'Small', text="Hotdogs are great") #Different size and message
