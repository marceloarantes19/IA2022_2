import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.datasets import load_iris
from sklearn import tree

clf = tree.DecisionTreeClassifier(random_state=0)
iris = load_iris()

print(iris.data, iris.target)
clf = clf.fit(iris.data, iris.target)

print(tree.export_text(clf))