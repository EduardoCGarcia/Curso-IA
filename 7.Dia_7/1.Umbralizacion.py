import cv2 #computer vision
import matplotlib.pyplot as plt 
import numpy as np


img = cv2.imread('images/gradiente.png',cv2.IMREAD_GRAYSCALE)
# Usando un umbral fijo
ret,img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,img3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # trunca lo que esta por debajo de 127 lo deja en blanco
ret,img4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,img5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titulos=['Original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
imgs=[img,img1,img2,img3,img4,img5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imgs[i],cmap='gray')
    plt.title(titulos[i])
    plt.xticks([]) # No se vean las escalas
    plt.yticks([])


plt.waitforbuttonpress()