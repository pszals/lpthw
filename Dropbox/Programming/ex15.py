# From the system (python program?) imports the argument variable module,
# providing the feature of having the user input a variable into the command line
from sys import argv

# Defines the variables "script" and "filename" as the argument variables
script, filename = argv

# Defines "txt" variable as the command "open()" with the variable filename inside
txt = open(filename)

# Displays text, calling on the filename variable with the format character %s
print "Here's your file %s:" % filename
# Prints the variable "txt" (which is a file called 'filename') with the 
# command to read it with no parameters. The '.' 
# attaches the command to the variable
print txt.read()

# Prompts user to type file name again
print "Type the filename again:"
# Defines variable "file_again" as some raw input from the user with a caret
file_again = raw_input("> ")

# Defines variable "txt_again" as the command "open()_" with the 
# variable txt_again inside
txt_again = open(file_again)
# Prints file "txt_again" with command to read it with no parameters
print txt_again.read()
print open(filename).read()