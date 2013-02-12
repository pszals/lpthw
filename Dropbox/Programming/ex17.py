# Unpacks our handy 'argv' code
from sys import argv
# Unpacks the 'exists' module, don't know what that does yet
from os.path import exists

# Defines our variables
script, from_file, to_file = argv

# Another use of format characters with our inputed by user files
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how? HAHAH! Like so:
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()

# Uses the 'len()' command, counts number of characters in file and returns number
print "The input file is %d bytes long" % len(indata)

# Apparently 'exists()' checks to see if a file exists
print "Does the output file exist? %r" % exists(to_file)
# If user hits RETURN, then program continues
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Opens 'to_file' in writeable mode as variable 'out_file'
out_file = open(to_file, 'w')
# 'out_file' is our open file in writeable mode, and variable
# 'indata' is being written to it
out_file.write(indata)

print "Alright, all done."

out_file.close()