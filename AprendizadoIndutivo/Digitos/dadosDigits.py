from sklearn import datasets # o Sklearn traz um conjunto de exemplos
from sklearn import svm
digits = datasets.load_digits() # Digits é dos exemplos
print("\nConjunto de dados\n",digits.data)
print("\nObjetivos\n", digits.target)
for i in range(0, 10):
	print("\nUma imagem isolada - Posição: ",i,"\n", digits.images[i])

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))