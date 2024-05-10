from Vertice import Vertice
from Aresta import Aresta
class Grafo:
	def __init__(self):
		self.__vertices = list()
		self.__arestas = list()
	def getVertices(self):
		return self.__vertices
	def setVertices(self, v):
		self.__vertices = v
	def getArestas(self):
		return self.__arestas
	def setArestas(self, a):
		self.__arestas = a
	def verticeExiste(self, v):
		return v in self.__vertices
	def verticeExistePorNome(self, n):
		for i in self.__vertices:
			if i.getNome() == n:
				return i, True
		return None, False
	def getVerticePorNome(self, n):
		for i in self.__vertices:
			if i.getNome() == n:
				return i
		return None
	def arestaExiste(self, vo, vd):
		for i in self.__arestas:
			if vo == i.getOrigem() and vd == i.getDestino():
				return True
		return False
	def insereVertice(self, n, val=0, p=0):
		v = Vertice(n, val, p)
		self.__vertices.append(v)
		return v
	def insereAresta(self, no, nd, vo=0, vd=0, po=0, pd=0, valor=0, tipo=1): # tipo = 1 --> Grafo e tipo = 2 --> Digrafo
		verticeOrigem, achou = self.verticeExistePorNome(no)
		if not achou:
			verticeOrigem = self.insereVertice(no, vo, po)
		verticeDestino, achou = self.verticeExistePorNome(nd)
		if not achou:
			verticeDestino = self.insereVertice(nd, vd, pd)
		if not self.arestaExiste(verticeOrigem, verticeDestino):
			aresta = Aresta(verticeOrigem, verticeDestino, valor)
			self.__arestas.append(aresta)
			if tipo == 1:
				aresta = Aresta(verticeDestino, verticeOrigem, valor)
				self.__arestas.append(aresta)
	def getSucessor(self, vertice):
		vizinhos = list()
		for i in self.__arestas:
			if i.getOrigem() == vertice:
				vizinhos.append(i.getDestino())
		return vizinhos
	def getSucessorPorNome(self, nome):
		vertice = None
		for i in self.__vertices:
			if i.getNome() == nome:
				vertice = i 
				break
		if vertice != None:
			return self.getSucessor(vertice)
		return None
	def mostraGrafo(self):
		for i in self.__vertices:
			x = i.getNome() + " --"
			for j in self.getSucessor(i):
				x = x + "- "+j.getNome()+" "
			print(x)
