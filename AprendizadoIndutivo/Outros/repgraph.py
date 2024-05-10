from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model # Carrega o modelo de regressão linear
from sklearn.metrics import mean_squared_error, r2_score # Computa a perforance do modelo

dia = datasets.load_diabetes()
print(dia.DESCR)
X = dia.data
Y = dia.target
NX = []
for i in X:
	nn = []
	nn.append(i[2])
	nn.append(0)
	NX.append(nn)

#Preparando testes e treinamento
xTreino, xTeste, yTreino, yTeste = train_test_split(NX, Y, test_size=0.2)

#Inserindo o modelo de regressão linear
modelo = linear_model.LinearRegression() # associa o modelo auma variável
modelo.fit(xTreino, yTreino) # Executa o Treinamento
yPrevisao = modelo.predict(xTeste) # Executa as previsões no conjunto de teste

# Verificando os resultados
print("Erro médio %.2f" % mean_squared_error(yTeste, yPrevisao))
print("Coeficiente de determinação %.2f" % r2_score(yTeste, yPrevisao))

from matplotlib import pyplot as plt
plt.scatter(xTeste, yTeste, label='Dados de Teste', color='r', alpha=.7)
plt.scatter(xTreino, yTreino, label='Dados de Treinamento', color='g', alpha=.7)
plt.plot(xTeste, yPrevisao, label='Regressão Linear', color='b')
plt.legend()
plt.show()
