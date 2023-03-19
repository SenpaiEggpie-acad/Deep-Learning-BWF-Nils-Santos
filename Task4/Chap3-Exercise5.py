#Made by Nils Santos
guest_list = ['Tony Stark', 'Tom Cruise', 'Angelina Jolie',
              'Albert Einstein', 'Nikola Tesla', 'Michael Jordan']
#First set of invitations
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[0]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[1]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[2]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[3]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[4]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[5]))
print("\n")

#Absent guest
absentee = guest_list.pop()
print("Sadly, {absent} cannot make it to the party \n".format(absent=absentee))

#New guest
guest_list.append("Justin Bieber")

#Second set of invitations
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[0]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[1]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[2]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[3]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[4]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[5]))