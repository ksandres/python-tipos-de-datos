# Lectura del valor de 2 variables enteras por consola:
print("Ingrese el número 1")
numero1 = int(input())
print("Ingrese el número 2")
numero2 = int(input())
print("Ingrese la operación (+, -, *, /)")
operacion = input()

if operacion == '+':
    # Operación suma:
    suma = numero1 + numero2
    print("La suma es " + str(suma))
elif operacion == '-':
    # Operación resta:
    resta = numero1 - numero2
    print("La resta es " + str(resta))
elif operacion == '*':
    # Operación multiplicación:
    multiplicacion = numero1 * numero2
    print("La multiplicación es " + str(multiplicacion))
elif operacion == '/':
    # Operación división:
    division = numero1 / numero2
    print("La división es " + str(division))
