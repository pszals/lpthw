from sys import argv

script, user_name, user_mood = argv

prompt = ">>"

print "Hi there %s, you are running the %s script!" % (user_name, script)
print "I'm going to ask you some questions now, %s." % user_name
print "What is making you feel %s today?" % user_mood

source_of_mood = raw_input(prompt)

print "That makes sense that %s has such an effect, %s." % (
	source_of_mood, user_name)
	
print "What should you do about the way you feel, %s?" % user_name

solution = raw_input(prompt)

print """
I feel ya, %s ! %s will surely be good for your %s mood!
""" % (user_name, solution, user_mood)



