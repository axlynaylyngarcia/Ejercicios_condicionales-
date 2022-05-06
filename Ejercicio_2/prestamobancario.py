"""Ejercicio 2

programacia que permita realizar un préstamo bancario, teniendo en cuenta que el 
préstamo será otorgado solamente a personas con ingresos superiores a $945200
y que no posea otra deuda"""

ingresos=int(input("Ingrese su sueldo: "))
#processing
if ingresos>945200:
    deudas=int(input(" ¿ Tienes deudas? Escriba 0 para no. 1 para si: "))
    if deudas==0:
        print("Se aprueba el préstamo")
    else:
        print("No se aprueba el préstamo")
else:
    print("No se aprueba el préstamo")     
    