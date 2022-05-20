import pandas as pd


data = pd.read_csv("res/binpacking1.csv")
print(type(data.columns[0]))

num = data[data.columns[0]].to_numpy()

print(num)
print(type(num))
print(num.shape)