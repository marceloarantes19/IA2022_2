from Vertice import Vertice
class Aresta:
	def __init__(self, ori = None, dest = None, valor = 0):
		self.__origem = ori
		self.__destino = dest
		self.__valor = valor
	def getOrigem(self):
		return self.__origem
	def setOrigem(self, o):
		self.__origem = o
	def getDestino(self):
		return self.__destino
	def setDestino(self, d):
		self.__destino = d
	def getValor(self):
		return self.__valor
	def setValor(self, n):
		self.__valor = n

