import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,3,4,5,6,7,9])
y=np.array([4,7,2,4,7,8,3])

x1=np.array([1,3,4,5,6,7,9])
y1=np.array([6,9,4,7,8,9,8])

plt.plot(x,y,'o') #Colocamos 'o' como marcador
plt.show()
input()
plt.plot(x,y,linestyle='dotted') #Colocamos 'o' como marcador
plt.show()
input()
plt.bar(x,y,label='Barra',color='g') #grafico de barra
plt.show()
input()
plt.plot(x,y,x1,y1)
plt.show()
input()

"""plt.plot(y)
plt.plot(y1)
plt.title('Edades vs Estaturas') #Titulo de la grafica
plt.xlabel('Edades')
plt.ylabel('Estaturas')
plt.grid() #Solo se ve la rejilla en las x si se quita el axis lo hace para todas
plt.show()"""
plt.subplot(1,2,1)#renglon, numero de columnas columna, en que renglos lo coloca
plt.plot(y)
plt.subplot(1,2,2)#renglon, numero de columnas columna, en que renglos lo coloca
plt.plot(y1)
plt.show()
