# Deckare a variable "cars" with value 100
cars = 100

# Deckare a variable "space_in_a_car" with value 4.0 or 4
space_in_a_car = 4.0

# Deckare a variable "drivers" with value 30
drivers = 30

# Deckare a variable "passengers" with value 100
passengers = 90

# Declare a variable for storing the numbers of cars without drivers
cars_not_driven = cars - drivers

# Deckare a variable to store number of cars with drivers
cars_driven = drivers

# Deckare a variable to store carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# Deckare a variable to find average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There wil be ", cars_not_driven, "emoty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have ", passengers, "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."