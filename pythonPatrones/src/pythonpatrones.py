# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
import filtros

imagenes = filtros.Filtros("cul.jpg").mi_filtro()
cv2.imwrite("nooo.jpg", imagenes)
cv2.imshow("cierre.jpg", imagenes)
cv2.waitKey(0)
