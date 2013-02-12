class Parent(object):
	def override(self):
		print "Parent Override"

class Child(object):
	def override(self):
		print "Child Override"
		
dad = Parent()
son = Child()

dad.override()
son.override()

print "-----"

