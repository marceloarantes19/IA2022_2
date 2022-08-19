from Fila import Fila
from MapaDaRomenia import Mapa

def largura(o, d, g):
  fila = Fila()
  fila.enfileira(o)
  while not fila.filaVazia():
    atual = fila.desefileira()
    print(atual.getNome())
    if atual == d:
      print("encontrei")
      return True
    else:
      for i in g.getSucessor(atual):
        fila.enfileira(i)
  return False

m = Mapa()
m.geraMapa()
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de Destino =: ")
ori, oex = m.verticeExistePorNome(origem)
des, dex = m.verticeExistePorNome(destino)
if oex and dex:
  largura(ori, des, m)