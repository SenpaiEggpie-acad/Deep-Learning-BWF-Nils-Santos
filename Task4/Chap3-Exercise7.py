#Made by Nils Santos
guest_list = ['Tony Stark', 'Tom Cruise', 'Angelina Jolie',
              'Albert Einstein', 'Nikola Tesla', 'Michael Jordan']
guest_list.insert(0,'Homer Simpson')
guest_list.insert(4,'Peter Griffin')
guest_list.append('Jackie Chan')

#First set of invites
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[0]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[1]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[2]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[3]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[4]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[5]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[6]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[7]))
print("Hello {guest}, you are invited to my birthday to dinner.".format(guest=guest_list[8]))
print("\n")

print("Attention. Due to issues with the tables, I can only accomodate two guests\n")
#Removal of guests
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
removed_guest=(guest_list.pop())
print("Sorry {guest}, your invitation is cancelled.".format(guest=removed_guest))
print("\n")

#Reconfirmation of invites
print("{guest}, you are still invited.".format(guest=guest_list[0]))
print("{guest}, you are still invited.".format(guest=guest_list[1]))
del guest_list[0]
del guest_list[0]
print("Guest list:"+str(guest_list))
