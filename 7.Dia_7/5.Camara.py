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
    
    frame=cv2.flip(frame,1) #Giramos al pantalla
    frame =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Ponemos la pantalla en escala de grises
    # Aplicamos el filtro adaptativo
    frame=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c==27: #Codigo
        break
cv2.release()
cv2.destroyAllWindows()