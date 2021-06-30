# Segmentar una image: Estraer regiones de interes
# Umbral: Valor que permite tomar el objeeto de interes


import cv2 #computer vision
import matplotlib.pyplot as plt 
import numpy as np


img = cv2.imread('images/Costa.jpg',cv2.IMREAD_COLOR)
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#m=np.ones(imgRGB.shape,dtype='uint8')*50
#Mejorar el contraste
m=np.ones(imgRGB.shape)*0.8
m2=np.ones(imgRGB.shape)*1.2
#img1=cv2.add(imgRGB,m)
#img2=cv2.subtract(imgRGB,m)

img1=np.uint8(cv2.multiply(np.float64(img),m))
img2=np.uint8(np.clip(cv2.multiply(np.float64(img),m2),0,255))#Lo ultimo es para indicar que los valores van de 0 a 255 para que los normalice

"""plt.subplot(131);plt.imshow(imgRGB);plt.title('Original')
plt.subplot(132);plt.imshow(img1);plt.title('Clara')
plt.subplot(133);plt.imshow(img2);plt.title('Oscura')"""

plt.subplot(131);plt.imshow(img1);plt.title('Bajo contraste')
plt.subplot(132);plt.imshow(img);plt.title('Original')
plt.subplot(133);plt.imshow(img2);plt.title('Alto contraste')

#plt.imshow(imgRGB)
plt.waitforbuttonpress()


