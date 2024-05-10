import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from PIL import Image
import numpy as np 

# Carregando a base de dados:
df_mnist = pd.read_csv('sample_data/mnist_train_small.csv', sep=',', index_col=0)
print(df_mnist.shape)