class Pilha:
  def __init__(self):
    self.__pilha = []
  def pilhaVazia(self):
    return len(self.__pilha) == 0
  def empilha(self, v):
    self.__pilha.append(v)
  def desempilha(self):
    if not self.pilhaVazia():
      return self.__pilha.pop()
