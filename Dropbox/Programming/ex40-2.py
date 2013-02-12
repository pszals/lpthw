# Defines class Song
class Song(object):
# Song has-a __init__ that takes the parameters self and lyrics
	def __init__(self, lyrics):
# From self get lyrics and set it to lyrics
		self.lyrics = lyrics
# Song has-a sing_me_a_song function that takes the parameter self
	def sing_me_a_song(self):
# For each line in from self get lyrics
		for line in self.lyrics:
# Print the line
			print line
# Set happy_bday to an instance of class Song that takes a list as parameter
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
# Set bulls_on_parade to an instance of class Song that takes a list of parameters
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
# On happy_bday get the sing_me_a_song function and call it with no parameters
happy_bday.sing_me_a_song()
# On bulls_on_parade get the sing_me_a_song function and call it with no parameters
bulls_on_parade.sing_me_a_song()