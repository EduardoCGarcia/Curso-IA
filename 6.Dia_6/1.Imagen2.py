import cv2 #computer vision
import matplotlib.pyplot as plt #usa diferentes mapas de color

#8 bits sin signo  (00000000 - 1111111) 2^8=256 (0-255) (negro - blanco)
img = cv2.imread('images/img1.png')#El segundo paramentro indica como la vas a leer RGB(0) SG(1) ALPHA(-1)
imgInv=img[:,:,::-1] #Esta es una de las fromas de cambier el modelo de color de BGR a RGB
r,g,b=cv2.split(imgInv)




plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r,cmap='gray');plt.title('Canal rojo')
plt.subplot(142);plt.imshow(g,cmap='gray');plt.title('Canal verde')
plt.subplot(143);plt.imshow(b,cmap='gray');plt.title('Canal azul')
img2 = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(img2[:,:,::-1]);plt.title('Unidos')


plt.waitforbuttonpress()

#python maneja el mapa de color como BGR


"""
IMAGENES
* Escala de grises
* RGB----BGR
"""