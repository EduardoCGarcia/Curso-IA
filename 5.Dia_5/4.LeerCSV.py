import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
#print(df.to_string())
#df.plot()
#df.plot(kind='scatter',x='Duration',y='Calories')
df['Duration'].plot(kind='hist')
plt.show()

#para un json
#pd.read_json()

#API REST:GET PORT PUT DELETE

