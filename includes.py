from ast import List
from dataclasses import field
from re import L
from data import File


class Includes:
	def __init__(self, file: File) -> None:
		self.include_list: list = []
		self.includes: str = ""


		self.file: File = file

		self.find_includes()
		# TODO : self.check_auth()
		self.normify()

		print(self.includes)


	def find_includes(self):
		for line in self.file.lines:


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

	def normify(self):
		for line in self.include_list:
			self.includes += line.replace(" ", "")


Includes(File('test.c'))