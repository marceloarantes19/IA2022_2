from Grafo import Grafo
class Mapa(Grafo):
	def geraMapa(self):
		self.insereVertice("Arad")
		self.insereVertice("Bucharest")
		self.insereVertice("Craiova")
		self.insereVertice("Dobreta")
		self.insereVertice("Eforie")
		self.insereVertice("Fagaras")
		self.insereVertice("Giurgiu")
		self.insereVertice("Hirsova")
		self.insereVertice("Iasi")
		self.insereVertice("Lugoj")
		self.insereVertice("Mehadia")
		self.insereVertice("Neant")
		self.insereVertice("Oradea")
		self.insereVertice("Pitesti")
		self.insereVertice("Rimnico Vilcea")
		self.insereVertice("Sibiu")
		self.insereVertice("Timisoara")
		self.insereVertice("Urziceni")
		self.insereVertice("Vaslui")
		self.insereVertice("Zerind")

		self.insereAresta("Arad","Zerind")
		self.insereAresta("Arad","Sibiu")
		self.insereAresta("Arad","Oradea")

		self.insereAresta("Bucharest","Fagaras")
		self.insereAresta("Bucharest","Pitesti")
		self.insereAresta("Bucharest","Giurgiu")
		self.insereAresta("Bucharest","Urziceni")

		self.insereAresta("Craiova","Pitesti")
		self.insereAresta("Craiova","Dobreta")
		self.insereAresta("Craiova","Rimnico Vilcea")

		self.insereAresta("Dobreta","Mehadia")

		self.insereAresta("Eforie","Hirsova")

		self.insereAresta("Fagaras","Sibiu")

		self.insereAresta("Hirsova","Urziceni")

		self.insereAresta("Iasi","Neant")
		self.insereAresta("Iasi","Vaslui")

		self.insereAresta("Lugoj","Mehadia")
		self.insereAresta("Lugoj","Timisoara")

		self.insereAresta("Oradea","Zerind")
		self.insereAresta("Oradea","Sibiu")

		self.insereAresta("Pitesti","Rimnico Vilcea")

		self.insereAresta("Rimnico Vilcea","Sibiu")

		self.insereAresta("Vaslui","Urziceni")
