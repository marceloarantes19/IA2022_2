from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model # Carrega o modelo de regressão linear
from sklearn.metrics import mean_squared_error, r2_score # Computa a perforance do modelo

dia = datasets.load_diabetes()
print(dia.DESCR)

X = dia.data
Y = dia.target

#Preparando testes e treinamento
xTreino, xTeste, yTreino, yTeste = train_test_split(X, Y, test_size=0.2)

#Inserindo o modelo de regressão linear
modelo = LinearRegression() # associa o modelo auma variável
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
#plt.scatter(b, yTreino, label='Dados de Treinamento', color='g', alpha=.7)
#plt.plot(a, yPrevisao, label='Regressão Linear', color='b')
plt.legend()
plt.show()
