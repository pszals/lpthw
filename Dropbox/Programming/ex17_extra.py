from sys import argv

script, from_file, to_file = argv

print "Copied %s to %s" % (from_file, to_file)

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
