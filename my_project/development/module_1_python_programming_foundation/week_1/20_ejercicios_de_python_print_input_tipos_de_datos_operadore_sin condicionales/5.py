#Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.
palabra = input("!!! Por favor ingresa una palabra: ")
num1 = int(input("Por favor ingresa un numero: "))

for i in range(num1):
    print(f"{palabra}")