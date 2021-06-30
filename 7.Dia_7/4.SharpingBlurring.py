import cv2 #computer vision
import numpy as np

img = cv2.imread('images/carro.jpg')
cv2.imshow('Imagen original',img)
cv2.waitKey()

imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagen Grises',img)
cv2.waitKey()

#Sharping

#filtro = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]) #Filtro
filtro = np.ones(3,3)/9

imgSharpered = cv2.filter2D(imGray,-1,kernel=filtro)#-1 misma profundidad que la  imagen de entrada que la de salida

cv2.imshow('Imagen con Filtro ',imgSharpered)
cv2.waitKey()

cv2.destoyAllWindows()