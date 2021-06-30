import cv2 #computer vision
import matplotlib.pyplot as plt 
import numpy as np

# Usando un umbral adaptativo
img = cv2.imread('images/Musica.png',cv2.IMREAD_GRAYSCALE)

ret,img1 = cv2.threshold(img,20,255,cv2.THRESH_BINARY)

img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
img3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


titulos=['Original','UMBRAL GLOBAL','ADAPTATIVE_THRESH_MEAN_C','ADAPTATIVE_THRESH_GAUSSIAN_C']
imgs=[img,img1,img2,img3]
for i in range(len(imgs)):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],cmap='gray')
    plt.title(titulos[i])
    plt.xticks([]) # No se vean las escalas
    plt.yticks([])


plt.waitforbuttonpress()