import cv2
import numpy as np
import sqlite3


con = sqlite3.connect('E:/PROGRAMACION/UNITY/Proyectos/Millennia World Map/Assets/DB.db')
def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('select Id, Red, Green, Blue from region where id between 10001 and 15000')

    rows = cursorObj.fetchall()
    
    print("Inicio");
    fic = open("pixelsMapUpdate.txt", "w")
    fic.close()

    for row in rows:
      
        print(row[0])
      
        # Load image, grayscale, Gaussian blur, threshold
        image = cv2.imread('img/regionsmap.png')
        r=row[1]
        g=row[2]
        b=row[3]
        bajos = np.array([b,g,r])
        altos = np.array([b,g,r])
        mask = cv2.inRange(image, bajos, altos)
        
        # Find contours
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        c = max(cnts, key=cv2.contourArea)
        
        # Obtain outer coordinates
        left = tuple(c[c[:, :, 0].argmin()][0])
        right = tuple(c[c[:, :, 0].argmax()][0])
        top = tuple(c[c[:, :, 1].argmin()][0])
        bottom = tuple(c[c[:, :, 1].argmax()][0])
        
        # Draw dots onto image
        cv2.drawContours(image, [c], -1, (36, 255, 12), 2)
        cv2.circle(image, left, 8, (0, 50, 255), -1)
        cv2.circle(image, right, 8, (0, 255, 255), -1)
        cv2.circle(image, top, 8, (255, 50, 0), -1)
        cv2.circle(image, bottom, 8, (255, 255, 0), -1)   
        
        fic = open("pixelsMapUpdate.txt", "a")
        print('update Region set InitX={[0]}, InitY={[1]}, EndX={[0]}, EndY={[1]} where Red={} and Green={} and Blue={};'
                              .format(left, bottom, right, top, r, g, b), file=fic)
        fic.close()

sql_fetch(con)

print("Finalizado")




#cv2.imshow('image', image)
#cv2.waitKey()