# A partir de aqui comenzamos a usar funciones para poder hacer un proyecto integral
import cv2

def deteccionContornosCanny(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Canny(imagen,30,80)
    return imagen

def deteccionContornosLaplace(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Laplacian(imagen,cv2.CV_64F)
    return imagen

def deteccionContornosSobel(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Sobel(imagen,cv2.CV_64F,dx=1,dy=0,ksize=7)
    return imagen


cap=cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara...')

# Leer varias imagenes

while True:
    #Video: conjunto de imagenes
    ret,frame=cap.read()
    if not ret:
        break
    c=cv2.waitKey(1)
    if c==ord('c'):
        frame = deteccionContornosCanny(frame)
    if c==ord('l'):
        frame = deteccionContornosLaplace(frame)
    if c==ord('s'):
        frame = deteccionContornosSobel(frame)
    
    if c==27: #Codigo ESC
        break
    cv2.imshow('Camara',frame)
cv2.release()
cv2.destroyAllWindows()