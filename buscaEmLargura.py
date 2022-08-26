class BuscaEmLargura:
  def largura(self, o, d, g):
    fila       = []  # Gerência especial da Fila para a busca em Largura
    pai        = []  # Lista de Pais para dar o caminho
    inicioFila = -1  # Início da fila
    fila.append(o)   # Adicionei na fila - Não retirar mais
    pai.append(-1)   # A origem não tem pai
    while not inicioFila>=len(fila):
      inicioFila = inicioFila + 1
      atual = fila[inicioFila] # pega o primeiro elemento da fila
      print("Visitando:", atual.getNome())
      if atual == d:
        self.mostraCaminho(inicioFila, fila, pai)
        return True
      else:
        for i in g.getSucessor(atual):
          fila.append(i)
          pai.append(inicioFila)
    return False

  def mostraCaminho(self, inicioFila, fila, pai):
    if inicioFila == -1:
      print("\n\nCaminho ************************")
    else:
      self.mostraCaminho(pai[inicioFila], fila, pai)
      print(fila[inicioFila].getNome())

