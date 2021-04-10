import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("img/colores.jpg")

#Establecemos el rango m�nimo y m�ximo de BGR (Blue, Green, Red):
min_values = np.array([40,0,0])
max_values = np.array([255, 120, 120])
 
#Detectamos los p�xeles que estan dentro del rango que hemos establecido:
mask = cv2.inRange(img, min_values, max_values)
  
#Mostramos la imagen original y la m�scara:
cv2.imshow("Original", img)
cv2.imshow("M�scara", mask)
 
#Salimos pulsando cualquier tecla:
print("\nPulsa cualquier tecla para cerrar las ventanas\n")
cv2.waitKey(0)
cv2.destroyAllWindows()