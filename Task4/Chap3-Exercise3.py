#Made by Nils Santos
my_ride = "Nissan Skyline GTR"
statements = ["I want to buy a {ride}.",
              "I would like my {ride} to come in white.",
              "My {ride} is a fast car."]

print(statements[0].format(ride=my_ride))
print(statements[1].format(ride=my_ride))
print(statements[2].format(ride=my_ride))