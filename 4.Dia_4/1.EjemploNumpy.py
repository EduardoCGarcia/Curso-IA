import numpy as np

# Funciona igual que range(a,b,c)
#a = np.arange(5)
# Crea una lista comenzando en 5 hassta el 20 de 2 en 2
a = np.arange(5, 20, 2)
print('\na = np.arange(5,20,2): \n', a)

# Tipos de datos
b = np.array([10, 20, 30, 40], dtype=np.float16)  # Flotantes de 16 bits
b = np.array([10, 20, 30, 40], dtype='f2')

c = b.astype(np.int32)  # Cambia el tipo de dato
print('\nTipo de dato b: \n', b.dtype)
print('\nTipo de dato c: \n', c.dtype)

d = np.ones((3, 4))  # Creamos una matriz de unos de (3x4)
print('Matriz (3x4) ones d: \n', d)

e = np.zeros((3, 4, 2))  # Creamos una matriz de ceros de (3x4x2)
print('Matriz (3x4) ones: \n', e)

# Arreglo dinamico
f = np.random.random((3, 4))
print('Arreglo random: \n', f)
enteros = np.random.randint((2, 20))
print('Arreglo random enteros: \n', enteros)

print()
# llena con valores que necesite (dimenciones),de que numeros
g = np.full((5, 6), 5)
print('\nMatriz de 5x6 de 5: \n', g)
print('\nSuma de los elementos de la matriz anterior: ', g.sum())
print('\nNumero mas grande de la matriz anterior: ', g.max())

# Crea una lista de numeros del 0 al 23 | Los acomoda 2x3x4
h = np.arange(24).reshape(2, 3, 4)
# Si el numero de elementos no cohincide con la dimenciones pedidas mandara un error
print('\nMatriz[2x3x4] de 0 - 23: \n', h)
h = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32], [40, 41, 42]])
print('\nMatriz 3x3: \n', h)

rengs = np.arange(4)  # Renglones [0,1,2,3]
cols = np.array([0, 1, 2, 0])  # Columnas [0,1,2,0]
# Vamos a meter esos valores dentro de un arreglo h
# h[rengs,cols]: Entra a las coordenadas de los arreglos declarados anterior mente
# Primero entra a:[0,0]
# [1,1]
# [2,2]
# [3,0]
print('\nImprime h[rengs,cols]: \n', h[rengs, cols])
h[rengs, cols] += 100
print('\nSuma 100 a -> h[rengs,cols]: \n', h)

# Filtros
filtro = h > 21  # Comparando con un escalar Esto compara no se te olvide
# Lo que guarda es una matris booleana
print('\nFiltro bool de nums mayor a 21 de h[]: \n', filtro)

i = h[filtro]  # Guarda los que cumplen la regla
print('\nLos valores que tienen true en el filtro: \n', i)

h[h % 2 == 0] += 100  # A los pares sumales 100
print('\nDe h a los pares sumales 100: \n', h)

h2 = np.array([[10, 11, 12, 23], [20, 21, 22, 23], [
              30, 31, 32, 23], [40, 41, 42, 23], [50, 51, 52, 23]])
print(h2)
subh2 = h2[:3, 1:3] #De filas, de columnas
print('\nh2[:3, 1:3]:\n',subh2)
print('\nSumamos 10 a h2\n',h2+10)
print('\nMultiplicamos 10 a h2: \n',h2*10)
print('\nPromedio por columna: \n',h2.mean(axis=0))  # Promedio por columna a nivel estadistico
print('\nPromedio por fila: \n',h2.mean(axis=1))  # Promedio por fila a nivel estadistico

# Matriz de numeros aleatorios de 2 a 50 de 3x3
A = np.random.randint(low=2, high=50, size=(3, 3))
# Matriz de numeros aleatorios de 2 a 50
B = np.random.randint(low=2, high=50, size=(3, 3))
print('\nMatriz de numeros aleatorios de 2 a 50 de 3x3: \n',A)
print('\nMatriz de numeros aleatorios de 2 a 50 de 3x3: \n',B)
C = np.vstack((A, B))  # Como concatenar las dos matrices en 2 matrices
print('\nVertical (vstack): \n',C)
C2 = np.hstack((A, B))  # Como concatenar las dos matrices en 2 matrices
print('\nHorizontal (hstack): \n',C2)
