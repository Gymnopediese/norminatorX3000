from data import File

class CleanFunction():
	#TODO : differentes partie d'une fonction sont a clean.

	def __init__(self, file: File) -> None:
		# commmence par recuperer toute les variables
		pass

	def find_functions(self):
		for i, line in enumerate(self.file.lines):

			print(i, line)
			continue


			if line.__contains__("#include"):
				self.include_list += [line]
			elif line.__contains__("include") and line.__contains__("#"):
				idx_hashtag = line.find('#')
				idx_include = line.find('include')
				if not line[idx_hashtag+1:idx_include].isspace(): # verifie qu'il n'y a rien entre les deux 
					print("erreur, ambigus 'include' et '#' sur la meme ligne") # TODO throw error
				else:
					self.include_list += [line]
			elif line.__contains__("include"):
				print("erreur, ambigus 'include' ") # TODO throw error





	def clean_variables(self):
		# clean les variables : met en deux lignes les declarations en une, etc...
		pass


if True:
	CleanFunction(File('test.c'))