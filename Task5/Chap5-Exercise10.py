#Made by Nils Santos

current_users = ['Harvey', 'Mike', 'Louis', 'Donna', 'Rachel']
new_users = ['Jessica', 'rAcHeL', 'MIKE', 'Benjamin', 'Daniel']

for user in new_users:
    user = user.title()
    if user in current_users:
        print("Username is already taken")

    else: 
        print('Username is available')
    
        