from tensorflow import keras
import numpy as np
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

datos_entrenamiento = np.array([[0,0],[0,1],[1,0],[1,1]],dtype='float32')
datos_objetivo = np.array([[0],[1],[1],[0]],dtype='float32')

modelo=Sequential()
modelo.add(Dense(10,input_dim=2,activation='relu'))
modelo.add(Dense(1,activation='sigmoid'))
modelo.compile(loss='mean_squared_error',
                optimizer ='adam',
                metrics=['binary_accuracy'])
# Entrenamiento
modelo.fit(datos_entrenamiento,datos_objetivo,epochs=1000)

# Prueba (evaluar el modelo)
calif = modelo.evaluate(datos_entrenamiento,datos_objetivo)
print('%s: %.2f%%' % (modelo.metrics_names[1],calif[1]*100))
print(modelo.predict(datos_entrenamiento).round())

# Esta es una red neuronal para la compuerta XOR jaja