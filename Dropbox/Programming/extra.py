class Singalong(object):
	
	def __init__(self):
		self.songtext = songtext
	
	def karaoke(self):
		for line in self.songtext:
			print line

ohrwurm = Song(["Hallo, hallo", 
				"ich bin dein Ohrwurm", 
				"dein Ohrwurm!"])

margaritaville = Song(["Some people claim",
						"that there's a woman to blame",
						"but I know",
						"it's my own damn fault"])
