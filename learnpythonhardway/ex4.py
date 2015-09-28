#assigning a variable cars with value 100
cars = 100

#assigning 4.0 as a value to variable space_in_a_car
space_in_a_car = 4.0

#assigning 30 as a value to a variable drivers
drivers = 30

#assigning 90 as a value to variable passengers
passengers = 90

#calculating number of cars which are not driven by assigning the difference between the values stored in variables "cars" and "drivers" and assigning the value to "var cars_not_driven"
cars_not_driven = cars - drivers

#assigning "drivers" to variable "cars_driven"
cars_driven = drivers

#calculating "carpool_capacity" by multiplying "cars_driven" with "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car

#calculating average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
