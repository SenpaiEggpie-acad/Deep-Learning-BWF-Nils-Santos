#Made by Nils Santos
ticket_price = 0
while True:
    age = int(input("Enter age: "))
    

    if age < 3:
        ticket_price += 0
        print("Price: 0")
        print("Running total: " + str(ticket_price) + "\n")
    elif age >= 3 and age < 12:
        ticket_price += 10
        print("Price: 10")
        print("Running total: " + str(ticket_price) + "\n")
    elif age >= 12:
        ticket_price += 15
        print("Price: 15")
        print("Running total: " + str(ticket_price) + "\n")
    
