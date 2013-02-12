# Defines variable "cars" as having a value of 100
cars = 100
# Defines variable "space in a car" as having a value of 4
space_in_a_car = 4
#Defines number of drivers as 30
drivers = 25
#Defines passengers as 90
passengers = 90
# Defines variable cars_not_driven as "cars" minus "drivers"
cars_not_driven = cars - drivers
# Defines cars_driven equal to the number of drivers
cars_driven = drivers
# Defines maximum capacity in the carpool as cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"