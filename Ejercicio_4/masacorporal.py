"""Ejercicio 4
Programa que calcula el índice de masa corporal de una persona (IMC = perso[kg] / altura2 [m]) e indica"""

from imp import is_frozen


print("------------------")
print("-------IMC--------")
print("------------------")

#input
peso=int(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))

#processing
IMC=peso/(altura*altura)

#output 
if IMC<16:
    print("Su estado es: " + "Criterio de ingreso a hospital.")
else:
    if IMC>16 and IMC<17:
        print("Su estado es: " + "Infrapeso")
    else:
        if IMC>17 and IMC<18:
         print("Su estado es: " + "Bajo peso")
    else:
        if IMC>18 and IMC<25:
            print("Su estado es: " + "Peso normal (Saludable)")
        else: 
            if IMC>25 and IMC<30:
                print("Su estado es: " "Sobrepeso crónico(Obesidad de grado II)")
        else:
            if IMC<=30 and IMC<35:
                
