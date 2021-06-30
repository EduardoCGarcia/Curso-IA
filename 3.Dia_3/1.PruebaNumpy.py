import numpy as np

#Tambien podemos declarar tuplaspero seguiran sinedo del mismo tipo de datos
tupla = np.array((1,2,3,4))

#Dimencion 0
a=np.array(50)

#Dimencion 1
b = np.array([1,2,3,4])

#Dimencion 2
c=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])

#Dimencion 3
d=np.array([[[1,2,3,4],[5,6,7,8]],[[9,0,1,2],[4,5,6,7]]])

#Dimencion 5 || ndmin: nos permite crear la lista de n dimenciones
e = np.array([1,2,3,4],ndmin=5)

#.ndim: es la dimencion que tiene la lista

print('\na = ',a,'\nDimencion: ',a.ndim,'\ntipo: ',type(a))
print('\nb = ',b,'\nDimencion: ',b.ndim,'\ntipo: ',type(b))
print('\nc = ',c,'\nDimencion: ',c.ndim,'\ntipo: ',type(c))
print('\nd = ',d,'\nDimencion: ',d.ndim,'\ntipo: ',type(d))
print('\ne = ',e,'\nDimencion: ',e.ndim,'\ntipo: ',type(e))

#Para accesar a los datos se hace igual que en las listas normales
print('a = ',a)
print('b[0][1] = ',b[0])
print('c[0][3] = ',c[0][3],'o tambien c[0,3] = ',c[0,3])
print('d[0][3] = ',d[0][0][3])
print('e[0][0][0][0][0][0] = ',e[0][0][0][0][0])
print()
# Tambien podemos usar los slisy
print(b[-3:-1]) # 2,3
print(c[1,-1])
print(d[0,1,2])
print(c[1,1:4]) # 6,7,8

# Tipos de datos
print(b.dtype) #int32
f=np.array(['Juan','Maria'])
print(f.dtype) #Unicode 
b = np.array([1,2,3,4],dtype='f') #Podemos cambiar el tipo de dato (flotante)
print('b = ',b[-3:-1],'\nTipo de dato: ',b.dtype) #2. nos idica qque numeros de punto flotante

"""Que pasa cuando igualamos dos listas"""

g=b #Hacemos que g sea igual a b
b[2]=0 #esto modifica a los dos arreglos pues b apunta a una direccion de memoria y al igualarlos
        # ambas g y b apuntaran a la misma direccion de memoria
print(b)
print(g)

print(b.shape)#Imprime la forma que tiene ese arreglo (Tupla con cada indice que tiene el numero de elementos del arreglo)
print(e.shape)#Nos da las dimenciones de los arreglos 5 Dimenciones(1x1x1x1x4)
print(c.shape)

h=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(h)
i=h.reshape(3,4) # Redimenciona la lista a una de 3x4 3 grupos de 4
print(i)
