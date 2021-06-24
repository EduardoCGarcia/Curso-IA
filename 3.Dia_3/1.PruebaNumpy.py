import numpy as np
#Dimencion 0
a=np.array(50)
#Dimencion 1
b = np.array([1,2,3,4])
b1 = np.array((1,2,3,4))
#Dimencion 2
c=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])
#Dimencion 3
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
#Dimencion 5
e = np.array([1,2,3,4],ndmin=5)

print(a)
print (d)
print (e)
print('El numero de dimenciones es: ',e.ndim)
print(type(a))
print(type(b))
print(type(c))

print(b.dtype)