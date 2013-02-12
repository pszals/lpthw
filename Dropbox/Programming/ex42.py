## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Class Dog is-a Animal has-a __init__ that takes self and name parameters
class Dog(Animal):
	
	def __init__(self, name):
		## from self get the name attribute and set it to name
		self.name = name
		
## class Cat is-a Animal has-a __init__ that takes self and name parameters
class Cat(Animal):
	
	def __init__(self, name):
		## from self get the name attribute and set it to name
		self.name = name

## class Person is-a object has-a __init__ that takes self and name parameters
class Person(object):
	
	def __init__(self, name):
		## from self get the name attribute and set it to name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person has-a function __init__ that takes attributes self, name, and salary
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## from self get the salary attribute and set it to salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	
	def __init__(self, name):
		self.name = name

## Salmon is-a Fish
class Salmon(Fish):
	
	def __init__(self, name):
		self.name = name

## Halibut is-a Fish
class Halibut(Fish):
	
	def __init__(self, name):
		self.name = name


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## set frank to the function Employee and call it with the parameters "Frank" and 120000
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish("Flipper")

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut("Harry")

print "Franks's salary is", frank.salary
print "Mary's pet is", satan.name
print "Mary's name is", mary.name
