# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
import filtros

import numpy as np


imagenes = filtros.Filtros("cul.jpg")
#imagenes.mi_filtro()
#imagenes = imagenes.cierre()
#imagenes = imagenes.apertura()
#imagenes = imagenes.erosion()
imagenes = imagenes.dilatacion()
#imagenes = imagenes.gradiente()
#imagenes = imagenes.tophat1()


#imagenes.dos_grises()
"""El tiempo de ejecucion de opencv fue: 0.021999835968
El tiempo de ejecucion de propio fue: 178.450999975"""
cv2.imwrite("nooo.jpg", imagenes)
cv2.imshow("cierre.jpg", imagenes)
cv2.waitKey(0)

def mario():
    img_rgb = cv2.imread('mario.jpg')
    template = cv2.imread('moneda.jpg')
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]): 
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

    cv2.imwrite('result.png', img_rgb)
    
#mario()
