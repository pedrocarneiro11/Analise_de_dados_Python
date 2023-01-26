import pandas as pd

dataframe = pd.read_csv('planilha.csv')
print(dataframe.shape)
print(dataframe.columns)
print("\n")
print(dataframe.dtypes)
print("\n")
print(dataframe.tail)
print("\n")
print(dataframe.max())
