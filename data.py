from dataclasses import dataclass, field
from io import TextIOWrapper
from typing import List


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

@dataclass
class File:
	name: str
	# text: str
	lines: List[str] = field(default_factory=list)

	def __init__(self, file_path, name="") -> None:
		with open(file_path, 'r', encoding='utf-8') as f:
			self.lines = f.readlines()
			# self.text = f.read()