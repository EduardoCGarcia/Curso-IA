import cv2 #computer vision
import matplotlib.pyplot as plt #usa diferentes mapas de color

#8 bits sin signo  (00000000 - 1111111) 2^8=256 (0-255) (negro - blanco)
img = cv2.imread('images/img_18x18.png',cv2.IMREAD_GRAYSCALE)#El segundo paramentro indica como la vas a leer RGB(0) SG(1) ALPHA(-1)
cv2.imshow('Imagen',img)
print(img)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img,cmap='gray')
plt.waitforbuttonpress()

#python maneja el mapa de color como BGR


"""
IMAGENES
* Escala de grises
* RGB----BGR
"""