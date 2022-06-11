from data import File


class Header():
	def __init__(self, file: File, user: str) -> None:
		# var
		self.exist: bool
		self.is_clean: bool
		self.header: str = ''
		self.user = user		
		self.file = file
		self.header_infos = open("scr/header_infos.txt",'r').readlines() #TODO : le lien marche ??
		self.header_42 = open("scr/header_42.txt",'r').readlines()


		# logic
		self.check_header()

		if not self.exist:
			self.create_header()
		elif not self.is_clean:
			print("not clean...")
			# TODO clean plus tard
			self.clean_header()
		else:
			pass


	def check_header(self):
		# verifie la premiere ligne
		self.exist = self.header_infos[0] in self.file.text
		
	def clean_header(self):
		pass

	def create_header(self):
		
		now = datetime.datetime.now()

		for i in range(len(self.header_infos)):
			self.header_infos[i] = self.header_infos[i].replace('$',self.user) # TODO : dynamic + mail
			self.header_infos[i] = self.header_infos[i].replace('%',self.file.name) # sys.argv : return des infos sur le fichier
			self.header_infos[i] = self.header_infos[i].replace('!',str(now.year))
			self.header_infos[i] = self.header_infos[i].replace('<<',str(now.month))
			self.header_infos[i] = self.header_infos[i].replace('F',str(now.day))
			self.header_infos[i] = self.header_infos[i].replace('^',str(now.hour))
			self.header_infos[i] = self.header_infos[i].replace('&',str(now.minute))
			self.header_infos[i] = self.header_infos[i].replace('=',str(now.second))
			self.header_infos[i] = self.header_infos[i][:48]  
			self.header_infos[i]+=self.header_42[i]
		self.header = ''.join(self.header_infos)

