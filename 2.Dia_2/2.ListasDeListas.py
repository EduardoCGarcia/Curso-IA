lista=[[1,2,3],[4,5,6],[7,8,9]] # Matriz

#3x3x3
lista2=[
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,20,30],[40,50,60],[70,80,90]],
    [[100,200,300],[400,500,600],[700,800,900]]
]

"""for x in range(3):
    print(lista2[x][0][0])
print()
for y in range(3):
    print(lista2[0][y][0])
print()
for z in range(3):
    print(lista2[0][0][z])
print()"""

for x in range(3):
    for y in range(3):
        for z in range(3):
            print('{0:<10d}'.format(lista2[x][y][z]),end=' ')
        print()
    print()

    """Trabajar las listas de esta forma es muy lento
    por lo tanto hay que buscar la forma de que sea mas rapido
    pues para procesar las imagenes se necesita hace muy rapido
    por eso usaremos numpy"""