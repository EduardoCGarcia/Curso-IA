# Haar, Viola Joes, HOG
import cv2



cap=cv2.VideoCapture('images/video.avi')

if not cap.isOpened():
    raise IOError('No puede abrir la camara...')

#Cargamos el clasificador
car_cascade = cv2.CascadeClassifier('images/cars.xml')


while True:
    #Video: conjunto de imagenes
    ret,frame=cap.read()
    if not ret:
        break
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    carros = car_cascade.detectMultiScale(gray,1.1,1)

    for (x,y,w,h) in carros:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)



    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c==27: #Codigo ESC
        break
    
cv2.destroyAllWindows()