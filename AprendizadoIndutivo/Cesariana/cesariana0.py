import pandas as pd #1
from sklearn.model_selection import train_test_split #2
from sklearn import tree #3

arquivo = pd.read_csv('c:/users/marce/onedrive/documentos/testeml/cesariana2.csv', sep=";") #1
y = arquivo['Cesariana'] #1
x = arquivo.drop('Cesariana', axis = 1) #1
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size = 0.3) #2

modelo = tree.DecisionTreeClassifier() #3
modelo.fit(x_treino, y_treino)  #3

r = modelo.score(x_teste, y_teste)
print(r)

xk_teste = x_teste[0:5]
yk_teste = y_teste[0:5]

previsoes = modelo.predict(xk_teste)
print(previsoes)
print(yk_teste)

#print(x)