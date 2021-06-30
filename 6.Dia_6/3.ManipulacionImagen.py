import cv2 #computer vision
import matplotlib.pyplot as plt 

#img = cv2.imread('images/img_18x18.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/Barco.jpg',cv2.IMREAD_COLOR)

"""img2 = img.copy()
img2[2,2]=127
img2[2,3]=127
img2[3,2]=127
img2[3,3]=127"""

img2=img[200:400,300:600]
# Ahora vamos a agrandar la imagen que recortamos
"""plt.imshow(img2)
plt.waitforbuttonpress()"""
cv2.imshow('Imagen2',img2)
cv2.waitKey()


#img3=cv2.resize(img2,None,fx=2,fy=2)
img3=cv2.resize(img2,dsize=(100,200),interpolation=cv2.INTER_AREA)
"""plt.imshow(img3)
plt.waitforbuttonpress()"""
cv2.imshow('Imagen3',img3)
cv2.waitKey()

imgH=cv2.flip(1)
imgV=cv2.flip(0)
imgHV=cv2.flip(-1)


