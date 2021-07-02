# Haar, Viola Joes, HOG
import cv2

print(cv2.data.haarcascades) # Direccion de haarcascades
# C:\Users\eduar\Desktop\Curso IA\venv-CursoIA\lib\site-packages\cv2\data\

face_xml= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_xml= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# Lo aremos con la camara

def detectaRostro(gray,frame):
    rostros = face_xml.detectMultiScale(gray,1.3,5) # Regresa las posiciones del rostro alto y ancho
    # 1.3 es un factor si es mas pequeño detecta mas rostros
    # Mas grande detecta menos
    for (x,y,w,h)in rostros: # (x,y,ancho,alto)
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2) #dibujamos el cuadrito
        roiGray = gray[y:y+h,x:x+w] # En estas posiciones esta el rostro entonces no es necesario que busque en toda la imagen si podemos reducr la region de busqueda
        roiColor = frame[y:y+h,x:x+w] # los queremos en la imagen a color por lo tanto tambien necesitanoms la zona del rostro a color 
        ojos = eye_xml.detectMultiScale(roiGray,1.3,5)
        for (ex,ey,ew,eh) in ojos:
            cv2.rectangle(roiColor,(ex,ey),((ex+ew),(ey+eh)),(0,255,0),2)

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