from MapaDaRomenia import Mapa
from BuscaEmLargura import BuscaEmLargura

m = Mapa()
bl = BuscaEmLargura()
m.geraMapa()
print("*** Testa Busca em Largura ***\n")
origem = input("Digite a cidade de Origem.: ")
destino = input("Digite a cidade de Destino: ")
ori, oex = m.verticeExistePorNome(origem)
des, dex = m.verticeExistePorNome(destino)
if oex and dex:
  achou = bl.largura(ori, des, m)
  if not achou:
    print("Não encontrei o caminho!")
else:
  if not oex:
    print(origem, "não é um nome de vértice conhecido.")
  if not dex:
    print(destino, "não é um nome de vértice conhecido.")
