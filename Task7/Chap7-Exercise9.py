#Made by Nils Santos
sandwich_orders = ['clubhouse', 'pastrami',
                   'ham and cheese', 'pastrami','pulled pork',
                   'pastrami']
finished_orders = []
cursor = 0

print("Announcement: We have run out of pastrami")
while cursor <= len(sandwich_orders)-1:
    if sandwich_orders[cursor] == 'pastrami':
        sandwich_orders.pop(cursor)
    else:    
        print("Now serving " + sandwich_orders[cursor].title())
        finished_orders.append(sandwich_orders.pop(cursor))
        
    