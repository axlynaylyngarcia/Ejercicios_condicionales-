"""Ejercicio 1
programacion de coordenada cartesianas"""

X= int (input("Ingrese coordenadas en x: "))
Y= int (input("Ingrese coordenadas en y: "))
if (X > 0 and Y > 0):
    print("Punto en el primer cuadrante")

elif( X > 0  and Y < 0):
    print("Punto en el segundo cuadrante ")

elif(X < 0 and Y < 0):
    print("Punto en el cuarto tercer")

elif(X < 0 and Y > 0):
    print("Punto en el cuarto cuadrante")

elif X==0 and Y==0:
    print("El punto esta en el origen")