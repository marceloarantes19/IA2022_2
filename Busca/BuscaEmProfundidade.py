class BuscaEmProdundidade:
  def profundidade(self, o, d, g):
    pilha    = []
    pai      = []
    visitado = []
    pilha.append(o)
    pai.append(-1)
    topo = 0
    while len(pilha)>0:
      atual = pilha[topo]
      if atual == d:
        self.mostraCaminho(topo, pilha, pai)
        return True
      elif atual.getEstado() == 0 and not (atual in visitado):
        atual.setEstado(1)
        sucessores = g.getSucessor(atual)
        for i in sucessores:
          pilha.append(i)
          pai.append(topo)
        topo = topo + len(sucessores)
        visitado.append(atual)
      else:
        pilha.pop()
        pai.pop()
        topo = topo - 1
    return False

  def mostraCaminho(self, atu, pilha, pai):
    if atu == -1:
      print("\n\nCaminho ************* ")
    else:
      self.mostraCaminho(pai[atu], pilha, pai)
      print(pilha[atu].getNome())


