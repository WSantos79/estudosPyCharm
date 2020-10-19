import pandas as pd
import matplotlib.pyplot as plt
df_netflix = pd.read_csv('netflix.csv')

print(df_netflix.columns)
import matplotlib.pyplot as plt


df1 = df_netflix[['title', 'country', 'rating', 'date_added',  'release_year']]


#df1 = df_netflix[['title', 'type', 'release_year', 'rating']]
#print(df1.head(20))


#df1.plot(x='date_added', y='release_year', kind='bar')
#plt.show()

#df1.plot.scatter(x='rating', y='release_year')
#plt.show()
