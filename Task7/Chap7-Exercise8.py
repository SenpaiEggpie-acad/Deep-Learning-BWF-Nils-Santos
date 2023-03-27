#Made by Nils Santos
sandwich_orders = ['clubhouse', 'ham and cheese', 'pulled pork']
finished_orders = []
cursor = 0

while cursor <= len(sandwich_orders)-1:
    print("Now serving " + sandwich_orders[cursor].title())
    finished_orders.append(sandwich_orders.pop(cursor))
    