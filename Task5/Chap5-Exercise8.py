#Made by Nils Santos

usernames = ['admin', 'Peppa', 'George', 'Mummy', 'Daddy']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    
    else:
        print("Hello {u_name}, welcome back.".format(u_name=user))