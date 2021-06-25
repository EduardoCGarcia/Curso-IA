import numpy as np

#Funciona igual que range(a,b,c)
#a = np.arange(5)
a = np.arange(5,20,2)
print(a)

#Tipos de datos
b = np.array([10,20,30,40],dtype=np.float16)
b = np.array([10,20,30,40],dtype='f2')

c= b.astype(np.int32)
print(b.dtype)
print(c.dtype)

d=np.ones((3,4))
print(d)

e=np.zeros((3,4,2)) #3 Dimenciones
print(e)

#Arreglo dinamico 
f = np.random.random((3,4))
print(f)
f2 = np.random.randint((3,4))
print(f2)

g=np.full((5,6),5)
print(g)
print(g.sum())
print(g.max())

h=np.arange(24).reshape(2,3,4)
print(h)
print('\n\n')
h=np.array([[10,11,12],[20,21,22],[30,31,32],[40,41,42]])
print(h)

rengs =np.arange(4)
cols=np.array([0,1,2,0])
#[0,0][1,1][2,2][3,0]
"""print(h[rengs,cols])#renglon columna renglon columna
print()
h[rengs,cols] +=100
print(h)"""

#Filtros
filtro=h>21 #Comparando con un escalar Esto compara no se te olvide
#Lo que guarda es una matris booleana 
print(filtro)
print()
i=h[filtro] #Guarda los que cumplen la regla
print(i)

h[h%2==0] += 100 #A los pares sumales 100
print(h)

h2=np.array([[10,11,12,23],[20,21,22,23],[30,31,32,23],[40,41,42,23],[50,51,52,23]])
print(h)
subh=h2[:3,1:3]
print(subh)
print(h2+10)
print(h2*10)
print(h2.mean(axis=0)) #Promedio por columna a nivel estadistico
print(h2.mean(axis=1)) #Promedio por fila a nivel estadistico

print()

A=np.random.randint(low=2,high=50,size=(3,3 ))#Matriz de numeros aleatorios de 2 a 50
B=np.random.randint(low=2,high=50,size=(3,3 ))#Matriz de numeros aleatorios de 2 a 50
print(A)
print(B)
C=np.vstack((A,B))#Como concatenar las dos matrices en 2 matrices
print(C)
C2=np.hstack((A,B))#Como concatenar las dos matrices en 2 matrices
print(C2)