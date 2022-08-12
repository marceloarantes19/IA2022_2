from Grafo import Grafo
from Vertice import Vertice
x = Grafo()

# Cria Vértices
for i in ["a", "b", "c", "d", "e"]:
  x.insereVertice(i)

x.insereAresta("a", "b")
x.insereAresta("a", "d")
x.insereAresta("a", "e")
x.insereAresta("b", "c")
x.insereAresta("b", "e")
x.insereAresta("c", "e")
x.insereAresta("d", "e")

x.mostraGrafo()