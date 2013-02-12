class Song(object):
	
	def __init__(self, songtext):
		self.songtext = songtext
	
	def karaoke(self):
		for line in self.songtext:
			print line

ohrwurm_text = ["Hallo, hallo", 
				"ich bin dein Ohrwurm", 
				"dein Ohrwurm!"]

margaritaville_text = ["Some people claim",
						"that there's a woman to blame",
						"but I know",
						"it's my own damn fault"]

margaritaville = Song(margaritaville_text)

ohrwurm = Song(ohrwurm_text)

margaritaville.karaoke()