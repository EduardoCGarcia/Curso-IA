import cv2 #computer vision
import matplotlib.pyplot as plt #usa diferentes mapas de color

#8 bits sin signo  (00000000 - 1111111) 2^8=256 (0-255) (negro - blanco)
img = cv2.imread('images/img1.png')#El segundo paramentro indica como la vas a leer RGB(0) SG(1) ALPHA(-1)
#imgrgb=img[:,:,::-1] #Esta es una de las fromas de cambier el modelo de color de BGR a RGB
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(imgHSV)




plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h,cmap='gray');plt.title('Canal rojo')
plt.subplot(142);plt.imshow(s,cmap='gray');plt.title('Canal verde')
plt.subplot(143);plt.imshow(v,cmap='gray');plt.title('Canal azul')
img2 = cv2.merge((h,s,v))
img2=cv2.cvtColor(img2,cv2.COLOR_HSV2RGB)
plt.subplot(144);plt.imshow(img2);plt.title('Unidos')
cv2.imwrite('img_copy.png',img2)


plt.waitforbuttonpress()

#python maneja el mapa de color como BGR


"""
IMAGENES
* Escala de grises
* RGB----BGR
"""