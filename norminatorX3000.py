
import os

from data import File
from header import Header
#from clean_function import CleanFunction
from includes import Includes
		

def norme(path):
	pass
    # global lines
    # file = open(path)
    # lines = file.readlines()
    # tabs()
    # func()
    # signslr()
    # signsr()
    # keywordSpace()
    # finalClean()
    # header()
    # save(path)


class NorminatorX3000():
	""" 
	Class at the bottom of this programme.
	It will run everything in order to "Normify" your C code
	"""
	def __init__(self, file_path) -> None:
		self.render_str: str = ""
		self.output: str = ""
		self.file: File = File(open(file_path)) # TODO open with as ?

		""" 00 : the header 
		This class will check for a 42 header, modify it if wrong (or unactual) and generate it if absent
		It return a string	"""
		self.header = Header(self.file, 'qq') # TODO insert 
		# print(header.header)

		""" 01 : the includes 
		This class will check for includes (TODO if allowed ??),
		And return them as a string	"""
		self.includes = Includes()

		""" 02 : the functions
		Cette class va gerer toutes les fonctions a partir de la main() (s'il y en a une)
		et renvoyer un string	"""
		self.functions = CleanFunction()

		""" 03 : render it ! 
		This method will "concat" all parts of the file's code and generate or overwrite a file with all refactored ! """
		self.render()

		""" 04 : final check 
		"""
		self.final_check()


	def render(self):
		self.render_str = self.header + self.includes + self.functions
		self.output = "filerendu..."
		# TODO : rendre le fichier !!!

	def final_check(self):
		self.output = stream.read()

		if "-all" in sys.argv:
			stream = os.popen('norminette /Users/albaud/Desktop/temp/*')
		elif "-i" in sys.argv:
			print('norminette '+sys.argv[1])
			stream = os.popen('norminette '+sys.argv[1])
		else:
			stream = os.popen('norminette /Users/albaud/Desktop/temp/')
			file = open("temp.c",'r')