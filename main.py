import pandas as pd
import matplotlib.pyplot as plot

dataframe = pd.read_csv('planilha.csv', delimiter=",")
print(dataframe.shape)
print(dataframe.columns)
print("\n")
print(dataframe.dtypes)
print("\n")
print(dataframe.tail)
print("\n")
print(dataframe.max())
print("\n")
print(dataframe.dtypes)
print(list(dataframe.columns.tolist()))

print(dataframe['Year'].max())

plot.style.use("ggplot")
plot.xlabel("Year")
plot.ylabel("Population")

x = dataframe['Year']
y = dataframe['Population']
plot.plot(x, y, color='black')
plot.draw()
# plot.savefig("grafico.png") # gera uma figura png
plot.show()