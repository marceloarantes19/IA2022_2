class Vertice:
	def __init__(self, n = "", c = 0, val = 0, peso = 0, est = 0):
		self.__nome = n
		self.__chave = c
		self.__valor = val
		self.__peso = peso
		self.__estado = est # 0 - se está pilha, 1 - se foi expandido
	def getNome(self):
		return self.__nome
	def setNome(self, n):
		self.__nome = n
	def getChave(self):
		return self.__chave
	def setChave(self, c):
		self.__chave = c
	def getValor(self):
		return self.__valor
	def setValor(self, v):
		self.__valor = v
	def getPeso(self):
		return self.__peso
	def setPeso(self, p):
		self.__peso = p
	def setEstado(self, e):
		self.__estado = e
	def getEstado(self):
		return self.__estado
