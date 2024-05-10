from sklearn import datasets # o Sklearn traz um conjunto de exemplos
iris = datasets.load_iris()  # Iris é um deles
digits = datasets.load_digits() # Digits é outro
print(digits.data)
print("\n\n", digits.images[0])