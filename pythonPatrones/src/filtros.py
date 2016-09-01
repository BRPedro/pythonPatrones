# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import cv2
import numpy as np

__author__ = "PBR"
__date__ = "$01/09/2016 11:13:37 AM$"


class Filtros:
    
    def __init__(self, imagen):
        self.imagen = cv2.imread(imagen)
        self.gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)        
        self.data = np.array(self.imagen)
        
    def cierre(self):
        kernel9 = np.ones((9, 9), np.uint8)
        cierre = cv2.morphologyEx(self.gris, cv2.MORPH_CLOSE, kernel9)
        return cierre
    
    def apertura(self):
        kernel9 = np.ones((9, 9), np.uint8)
        apertura = cv2.morphologyEx(self.gris, cv2.MORPH_OPEN, kernel9)
        return apertura
     
    def erosion(self):
        kernel11 = np.ones((11, 11), np.uint8)
        erosion = cv2.erode(self.gris, kernel11, iterations=1)
        return erosion
    
    def dilatacion(self):
        kernel11 = np.ones((11, 11), np.uint8)
        dilatacion = cv2.dilate(self.gris, kernel11, iterations=1)
        return dilatacion
        
    def gradiente(self):
        ee3  = np.ones((3,3),np.uint8)
        gradiente =cv2.morphologyEx(self.gris, cv2.MORPH_GRADIENT,ee3)
        return gradiente
    
    
    def tophat(self):
        ee5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(200,200))
        tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT,ee5)
        return tophat
    
    def mi_filtro(self):
        newData = self.data
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                rojo,verde,azul=self.data[f][c]
                #promedio=(rojo+verde+azul)//3
                if (rojo < verde) and (azul < verde):
                    newData[f][c]=[0,255,0]
                else:
                    newData[f][c]=[255,255,255]
        cv2.imwrite('tem.jpg', newData)
        tem=cv2.imread('tem.jpg')
        return tem
        
    
        
         
        