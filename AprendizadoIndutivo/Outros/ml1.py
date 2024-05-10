from sklearn import tree
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
#labels = [chicken, chicken, horse, horse]
labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
 
print(classif.predict([[5, 400, 20]]))