import cv2 #computer vision
import matplotlib.pyplot as plt 
import numpy as np

# Usando un umbral adaptativo
imgRect = cv2.imread('images/rectangulo.jpg',cv2.IMREAD_GRAYSCALE)
imgCir = cv2.imread('images/circulo.jpg',cv2.IMREAD_GRAYSCALE)

# 1 & 1 = 1; otro caso nos da cero
imgAND = cv2.bitwise_and(imgRect,imgCir,mask=None)
imgOR = cv2.bitwise_or(imgRect,imgCir,mask=None)
imgXOR = cv2.bitwise_xor(imgRect,imgCir,mask=None)


plt.figure(figsize=[10,5])
plt.subplot(151);plt.title('Rectangulo');plt.imshow(imgRect,cmap='gray')
plt.subplot(152);plt.title('Circulo');plt.imshow(imgCir,cmap='gray')
plt.subplot(153);plt.title('AND RC');plt.imshow(imgAND,cmap='gray')
plt.subplot(154);plt.title('OR RC');plt.imshow(imgOR,cmap='gray')
plt.subplot(154);plt.title('XOR RC');plt.imshow(imgXOR,cmap='gray')
plt.xticks([]) # No se vean las escalas
plt.yticks([])
print(imgRect.shape)


plt.waitforbuttonpress()