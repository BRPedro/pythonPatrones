import cv2
import argparse

p = argparse.ArgumentParser("Muestra una imagen")
p.add_argument("archivo",default=None,action="store", 
    help="Nombre de archivo")
opts = p.parse_args()

img = cv2.imread("Image.png")

cv2.imshow("Mostrando imagen: "+opts.archivo,img)

print "Oprima una tecla para cerrar"
cv2.waitKey(0)