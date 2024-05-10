from sklearn import datasets
dia = datasets.load_diabetes()
#print(dia)
print(dia.DESCR)
#print(dia.feature_names)

X = dia.data
Y = dia.target
#B = dia.
print(X.shape," - ", Y.shape)

#Preparando testes e treinamento
from sklearn.model_selection import train_test_split
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.2)
print("Treino: ", xTreino.shape, " - ", yTreino.shape)
print("Testes: ", xTeste.shape, " - ", yTeste.shape)

#Inserindo o modelo de regressão linear
from sklearn import linear_model # Carrega o modelo de regressão linear
from sklearn.metrics import mean_squared_error, r2_score # Computa a perforance do modelo
modelo = linear_model.LinearRegression() # associa o modelo auma variável
modelo.fit(xTreino, yTreino) # Executa o Treinamento
yPrevisao = modelo.predict(xTeste) # Executa as previsões no conjunto de teste

# Verificando os resultados
print("Erro médio %.2f" % mean_squared_error(yTeste, yPrevisao))
print("Coeficiente de determinação %.2f" % r2_score(yTeste, yPrevisao))
x = yTeste
y = yPrevisao
a = []
b = []
for i in xTeste:
	a.append(i[2])

for i in xTreino:
	b.append(i[2])


from matplotlib import pyplot as plt
plt.scatter(a, yTeste, label='Dados de Teste', color='r', alpha=.7)
plt.scatter(b, yTreino, label='Dados de Treinamento', color='g', alpha=.7)
plt.plot(a, yPrevisao, label='Regressão Linear', color='b')
plt.legend()
plt.show()
