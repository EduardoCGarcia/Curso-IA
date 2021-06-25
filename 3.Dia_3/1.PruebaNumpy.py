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