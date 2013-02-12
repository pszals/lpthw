# We import our 'argv' function from sys
from sys import argv

# Here we name the two variables for 'argv'
script, input_file = argv

# Define 1st function with one variable that takes the 'f' from below
def print_all(f):
# Reads file 'f' and puts it into the print_all() function
	print f.read()

# Defines 2nd function, again with only one variable taking from below
def rewind(f):
# Seeks to the beginning of the 'f' file
	f.seek(0)

# Defines 3rd function, this time with two variables
def print_a_line(line_count, f):
# Takes line_count (user-inputed variable) and the current line
# being read, and inputs into the 'print_a_line' function
	print line_count, f.readline()

# Defines variable 'current_file' as the opening of the user-inputed file
current_file = open(input_file)

# Displays text with a new line after it
print "First let's print the whole file:\n"

# Uses function 'print_all' that reads and displays the user-inputed file
print_all(current_file)

# Displays another line of text
print "Now let's rewind, kind of like a tape."

# Uses the rewind function 'rewind' to put the reader at the beginning of the file
rewind(current_file)

# Displays more text
print "Let's print three lines:"

# Assigns 'current_line' variable value of 1 to the line count
current_line = 1
# Calls function 'print_a_line' and gives two variables
print_a_line(current_line, current_file)

# Assigns 'current_line' the value of the former 'current_line' plus 1
current_line += 1
# Calls function 'print_a-line' and gives two variables
# (The current_file opens the inputed file)
print_a_line(current_line, current_file)

# x += y works as x = x + y
# adds 1 to current line and defines current line variable at the same time
current_line += 1
print_a_line(current_line, current_file)