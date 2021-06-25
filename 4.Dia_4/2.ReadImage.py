import cv2

img = cv2.imread('images/background.jpg')
print(img.shape)
print(img.ndim)
print(img.shape[0])
cv2.imshow('imagen XIAO',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img[:,:,0] = 255


"""
Modelos de color
RGB


"""