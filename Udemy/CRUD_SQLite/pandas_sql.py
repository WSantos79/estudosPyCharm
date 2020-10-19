import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
"""conector = sqlite3.connect("meubanco.cu")

df = pd.read_sql_query("SELECT * FROM produtos", conector)

print(df.head())

df.plot(x='nome', y='preco', kind='bar')
plt.show()

df .plot.scatter(x='nome', y='preco')
plt.show()"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x, y)
plt.show()