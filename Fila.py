class Fila:
  def __init__(self):
    self.__fila = []
  def filaVazia(self):
    return len(self.__fila) == 0
  def enfileira(self, v):
    self.__fila.append(v)
  def desefileira(self):
    if not self.filaVazia():
      return self.__fila.pop(0)
