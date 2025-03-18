# Crea un programa que pida al usuario que ingrese números enteros hasta que ingrese el número 
# 0. Utiliza un ciclo while para pedir los números, y dentro del ciclo, utiliza una condicional if para 
# verificar si el número es negativo. Si el número es negativo, se debe imprimir un mensaje y 
# continuar pidiendo nuevos números con continue. Si el número ingresado es cero, el ciclo debe 
# terminar usando break y mostrar la cantidad de números positivos ingresados.

positives = 0
positive_numbers = []
while True:
    number = int(input("Ingresa un numero por favor: "))

    if number < 0:
        print("El numero es negativo, por favor sigue ingresando numeros")
        continue
    elif number == 0:
        break
    else:
        positives += 1
        positive_numbers.append(number)

print(f"\nSe ingresaron {positives} numero(s) positivos")
print(f"Los cuales fueron los siguientes: \n{positive_numbers}")