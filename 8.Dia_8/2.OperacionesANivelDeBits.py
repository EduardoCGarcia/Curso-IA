import cv2 #computer vision
import matplotlib.pyplot as plt 
import numpy as np

# Usando un umbral adaptativo
img= cv2.imread('images/LogoCocaCola.png')
imGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_,imgBin = cv2.threshold(imGray,127,255,cv2.THRESH_BINARY) #Con un _ no se guarda en ninguna variable si es que no se va a usar 
NotImgBin = cv2.bitwise_not(imgBin)

imgResult=cv2.bitwise_and(img,img,mask=NotImgBin)
#imgXOR = cv2.bitwise_xor(imgRect,imgCir,mask=None)

img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
imgResult=cv2.cvtColor(imgResult,cv2.COLOR_RGB2BGR)
plt.figure(figsize=[15,5])
plt.subplot(151);plt.title('CocaCola');plt.imshow(img,cmap='gray')
plt.subplot(152);plt.title('CocaCola Bin');plt.imshow(imgBin,cmap='gray')
plt.subplot(153);plt.title('CocaCola not Bin');plt.imshow(NotImgBin,cmap='gray')
plt.subplot(154);plt.title('CocaCola en negro');plt.imshow(imgResult,cmap='gray')



plt.waitforbuttonpress()