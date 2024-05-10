import pandas as pd #1
from sklearn.model_selection import train_test_split #2
from sklearn.ensemble import ExtraTreesClassifier #3
from sklearn import svm
arquivo = pd.read_csv('c:/users/marce/onedrive/documentos/testeml/Cesaria.csv', sep=";") #1
y = arquivo['Cesaria'] #1
x = arquivo.drop('Cesaria', axis = 1) #1
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size = 0.) #2
modelo = ExtraTreesClassifier() #3
modelo.fit(x_treino, y_treino)  #3

r = modelo.score(x_teste, y_teste)
print(r)

xk_teste = x_teste[0:5]
yk_teste = y_teste[0:5]

previsoes = modelo.predict(xk_teste)
print(previsoes)
print(yk_teste)