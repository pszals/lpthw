# Goes to the system, imports argument variables (input lines into bash)
from sys import argv

# Defines variables 'script' and 'filename' as the two argument variables
script, filename = argv

# Displays text phrase and variable format character 'r,' calls 'r' the filename argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Asks user for input, and displays a ? as a prompt
raw_input("?")

# Displays text
print "Opening the file..."
# Defines variable 'target' as the command to open the argv 'filename' in WRITE 
# mode. (Without the ", 'w'" after the filename, cannot manipulate file later.)
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
# Uses the target, which is defined as the opened argv 'filename' and uses '.'
# to attach the 'truncate()' command 
target.truncate()

print "Now I'm going to ask you for three lines."

# Defines three variables as three separate user inputs
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Recalls the 'target' variable and WRITES the inputed variables,
# each on their own new line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# Recalls the 'target' variable, which is the file inputed from user, 
# and closes it.
target.close()