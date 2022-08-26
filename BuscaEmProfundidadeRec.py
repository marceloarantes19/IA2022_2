class BuscaEmProdundidadeRec:
  def profundidadeRec(self, o, d, g):
    caminho  = []
    visitado = []
    achou, caminho = self.profundidade(o, d, g, visitado, caminho)
    if achou:
      print("\n\nCaminho ************* ")
      caminho.append(o)
      self.mostraCaminho(caminho)
      return True
    else:
      return False

  def profundidade(self, atual, destino, g, visitado, caminho):
    if atual == destino:
      return True, caminho
    elif not (atual in visitado):
      visitado.append(atual)
      for i in g.getSucessor(atual):
        if not i in visitado:
          ret = self.profundidade(i, destino, g, visitado, caminho) # Chamada Recursiva
          if ret:
            caminho.append(i)
            return True, caminho
    return False, []

  def mostraCaminho(self, caminho):
    if len(caminho) != 0:
      print(caminho.pop().getNome())
      self.mostraCaminho(caminho)


