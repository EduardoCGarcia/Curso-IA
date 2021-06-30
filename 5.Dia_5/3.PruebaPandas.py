import pandas as pd

#Serie
#DataFrame

a=[1,5,2]
print('La lista a:\n',a)
b = pd.Series(a) #Tambien los etiqueta 0,1,2,3,4,5,6,7,8,9...
print('Serie generada a partir de a:\n',b)
print('b[0]Serie: ',b[0]) #Asi se accede a la serie

#Podemos crear etiquetas en particular
b = pd.Series(a,index=['x','y','z']) # index tiene las nuevas etiquetas de la serie
print('\nNuevos indices de la serie:\n',b)
print('\nb[\"x\"]: ',b['x'])

#Las claves del diccionario se convierten en etiquetas
calorias={'Lunes':420,'Martes':300,'Miercoles':320}
c=pd.Series(calorias)
print(c)
print('Diccionario a Serie c[\'Martes\']: ',c['Martes'])

print('\nSolo usando algunas key del diccionario\n')
calorias={'Lunes':420,'Martes':300,'Miercoles':320}
d=pd.Series(calorias,index=['Lunes','Miercoles']) #Solo me llevo unos valores
print('Serie completa solo con dos indices:\n',d)


#DataFrame
print('\n\nD A T A    F R A M E')
datos={
    'Calorias':[420,300,320],
    'Duracion':[50,40,45]
}

e = pd.DataFrame(datos) # Como si se creara una tablita
print('DataFrame datos: \n',e)
""" Calorias  Duracion
0       420        50
1       300        40
2       320        45"""

#Accesar a una fila (loc trae las filas)
# Las filas consideran todas las key que tenia el diccionario (ahora un dataframe)
print('\nFila 1: \n',e.loc[0])
print('\nFila 2: \n',e.loc[1],)
print('\nFila 3: \n',e.loc[2])

print('\nTipo de dato de una de las filas: ',type(e.loc[0]))
print('\nTipo de dato del dataframe: ',type(e))
print('Podemos mostrar las filas que queramos como en los slice',e.loc[[0,1,2]]) #Muestra las que pidas
print(e.loc[:]) #Muestra todos


f = pd.DataFrame(datos,index=['Lunes','Martes','Miercoles']) # Como si se creara una tablita
print(f)
print(f.loc[:]) #Muestra todos

#Extenciones de archivo excel: xlsx
#Datos.xlsx
#datos.csv
#Un archivo de excel es un DataFrame


