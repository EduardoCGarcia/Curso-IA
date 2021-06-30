import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,3,4,5,6,7,9])
y=np.array([4,7,2,4,7,8,3])

x1=np.array([1,3,4,5,6,7,9])
y1=np.array([6,9,4,7,8,9,8])

#Tambien pueden ser colores en exadecimal (color='#00ff00') cada valor es de 4 bits
"""plt.scatter(x,y,color='#0000ff') #Solo muestra los puntos 2^24
plt.scatter(x1,y1) #Solo muestra los puntos
plt.show()


# HISTOGRAMA
x=np.random.normal(170,10,250)#Numeros en forma de campana de Gauss
print(x)
plt.hist(x) #Cantidad de valores encontro por y cuantas x por y
plt.show()"""

x=np.array([35,25,25,15])
etiquetas=['No aprobados','Regulares','Buenazos','Sobresalientes']
plt.pie(x,labels=etiquetas,startangle=90,explode=[0.2,0,0,0],shadow=True,autopct='%d%%')#desde que angulo comienza #Saca o extra un pedazo de la grfica
plt.legend(title='Alumnos')
plt.show()