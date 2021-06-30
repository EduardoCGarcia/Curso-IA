import cv2 #computer vision

img = cv2.imread('images/background.jpg')
print(img.shape)
print(img.ndim)
print(img.shape[0])
newimg=cv2.resize(img,(0,0),fx=0.25,fy=0.25) #Redimiencionamos la imagen para que se pueda ver mas completa
"""cv2.imshow('imagen XIAO',img)
cv2.imshow('new XIAO',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#si se ejecutan estas 3 la imagen se hacae blanca
#Dependiendo de cual se ejecute la matriz RGB sera modificada haciendose blanca
#newimg[:,:,0] = 255 
#cv2.imshow('BLUE XIAO',newimg)
#cv2.waitKey(0)
#newimg[:,:,1] = 255 
#cv2.imshow('GREN XIAO',newimg)
#cv2.waitKey(0)
#newimg[:,:,2] = 255 
#cv2.imshow('RED XIAO',newimg)
#cv2.waitKey(0)

#newimg[:,:,0] = 0 
#cv2.imshow('GREN XIAO',newimg)
#cv2.waitKey(0)
#newimg[:,:,1] = 0 
#cv2.imshow('RED XIAO',newimg)
#cv2.waitKey(0)
newimg[:,:,2] = 0 
cv2.imshow('BLUE XIAO',newimg)
cv2.waitKey(0)


cv2.destroyAllWindows()
"""
Modelos de color
RGB


"""