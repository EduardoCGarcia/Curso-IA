import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara...')

# Leer varias imagenes

while True:
    #Video: conjunto de imagenes
    ret,frame=cap.read()
    if not ret:
        break
    
    h,w = frame.shape[:2] #tupla que regresa 2 valores alto y ancho de la imagen
    #// solo nos da la perte entera del resultado
    centro=(w//2,h//2)
    MatrizdeGiro = cv2.getRotationMatrix2D(centro,-45,1)#centro,angle,scale
    #el giro lo hace la siguiente funcion
    frame = cv2.warpAffine(frame,MatrizdeGiro,(w,h))
    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c==27: #Codigo
        break
cv2.release()
cv2.destroyAllWindows()