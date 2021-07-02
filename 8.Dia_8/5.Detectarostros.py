# Haar, Viola Joes, HOG
import cv2

print(cv2.data.haarcascades) # Direccion de haarcascades
# C:\Users\eduar\Desktop\Curso IA\venv-CursoIA\lib\site-packages\cv2\data\

face_xml= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# Lo aremos con la camara

def detectaRostro(gray,frame):
    rostros = face_xml.detectMultiScale(gray,1.3,5) # Regresa las posiciones del rostro alto y ancho
    # 1.3 es un factor si es mas pequeño detecta mas rostros
    # Mas grande detecta menos
    for (x,y,w,h)in rostros: # (x,y,ancho,alto)
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2) #dibujamos el cuadrito
    return frame



cap=cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara...')

# Leer varias imagenes

while True:
    #Video: conjunto de imagenes
    ret,frame=cap.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = detectaRostro(gray,frame)
    
    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c==27: #Codigo ESC
        break
    
cv2.release()
cv2.destroyAllWindows()