import datetime
from abc import abstractclassmethod
from dataclasses import dataclass
from tkinter import N, Variable
from tkinter.messagebox import NO
from typing import List, Dict


def main():
	NorminatorX3000()
	
@dataclass
class Function:
	function_declaration: str
	variable_declaration: List[str] # numero ligne, content
	content_by_line: List[str] # TODO : voir comment on fait

@dataclass
class Data:
	header: str
	includes: List[str]
	fonctions: List[Function]

	



class NorminatorX3000():
	def __init__(self, file_path) -> None:
		self.file = open(file_path) # TODO dyn

		""" 00 : the header """
		header = Header(self.file, 'qq') # TODO insert 
		# print(header.header)

		""" 01 : the includes """


		""" 02 : the functions """


		""" 03 : the  """


		""" 04 : the  """


		""" 05 : the  """


		pass
	 

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



class Utils():
	@abstractclassmethod
	def OO(num):
		"""ajoute un 0 devant les chiffres """
		if num == 0:
			return '00'
		if num <10:
			return f'0{num}'
		return str(num)

class clean_function():
	#TODO : differentes partie d'une fonction sont a clean.

	def __init__(self) -> None:
		data = data_function()
		# commmence par recuperer toute les variables
		pass


	def clean_variables(self):
		# clean les variables : met en deux lignes les declarations en une, etc...
		pass

class Header():
	def __init__(self, file, user) -> None:
		# var
		self.exist: bool
		self.is_clean: bool
		self.header: str = ''

		self.user = user
		self.file_name = "file.name()" # TODO
		self.file_text = file.read()
		self.file_lines = file.readlines()
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
		self.exist = self.header_infos[0] in self.file_text
		
	def clean_header(self):
		pass

	def create_header(self):
		
		now = datetime.datetime.now()

		for i in range(len(self.header_infos)):
			self.header_infos[i] = self.header_infos[i].replace('$',self.user) # TODO : dynamic + mail
			self.header_infos[i] = self.header_infos[i].replace('%',self.file_name) # sys.argv : return des infos sur le fichier
			self.header_infos[i] = self.header_infos[i].replace('!',str(now.year))
			self.header_infos[i] = self.header_infos[i].replace('<<',str(now.month))
			self.header_infos[i] = self.header_infos[i].replace('F',str(now.day))
			self.header_infos[i] = self.header_infos[i].replace('^',str(now.hour))
			self.header_infos[i] = self.header_infos[i].replace('&',str(now.minute))
			self.header_infos[i] = self.header_infos[i].replace('=',str(now.second))
			self.header_infos[i] = self.header_infos[i][:48]  
			self.header_infos[i]+=self.header_42[i]
		self.header = ''.join(self.header_infos)



	
if __name__ == "__main__":
	main()
