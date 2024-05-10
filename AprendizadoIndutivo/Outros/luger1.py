# História de Crédito - Ruim (1), Desconhecida (2) e Boa (3)
# Dívida - Baixa (1) e Alta (2)
# Garantia - Nenhuma (1) e adequada (2)
# Renda - 0 a 15 (1), 15 a 35 (2) e acima de 35 (3) 
# Risco (variável alvo) - Baixo (1), Moderado (2) e Alto (3)

import pandas as pd 
import numpy as np 
from sklearn import tree
features = [
              [1,2,1,1], #1
              [2,2,1,2], #2
              [2,1,1,2], #3
              [2,1,1,1], #4
              [2,1,1,3], #5
              [2,1,2,3], #6
              [1,1,1,1], #7
              [1,1,2,3], #8
              [3,1,1,3], #9
              [3,2,2,3], #10
              [3,2,1,1], #11
              [3,2,1,2], #12
              [3,2,1,3], #13
              [1,2,1,2]  #14
       ]
labels = [3,3,2,3,1,1,3,2,1,1,3,2,1,3]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)

print(classif.predict([[2,2,2,3]]))

#tree.plot_tree(classif, filled=True)
#print(tree.export_text(classif))
