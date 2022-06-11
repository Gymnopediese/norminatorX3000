class Utils:
	@staticmethod
	def OO(num: int):
		""" ajoute un 0 devant les chiffres """
		if num == 0: return '00'
		if num <10:	return f'0{num}'
		return str(num)

	@staticmethod
	def is_in(scr: str, look: str):
		str.__contains__(look) ## TODO : inutile d'avoir une fonction pour ca...
		

	# @staticmethod
	# def :
	# 	pass

	# @staticmethod
	# def :
	# 	pass
	
	# @staticmethod
	# def :
	# 	pass
	