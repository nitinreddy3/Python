# Defined the variables 
people = 30
cars = 35
buses = 40

# If else to check the scenarios for transportation based on availability of buses and cars

if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can' decide.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ( "Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print ("Fine, let's stay home then.")