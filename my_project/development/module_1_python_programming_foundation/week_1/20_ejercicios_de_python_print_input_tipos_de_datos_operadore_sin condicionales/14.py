#Pide dos números y muestra si el primero es mayor que el segundo (usar operador de comparación).
num1 = int(input("Por favor ingresa un numero: "))
num2 = int(input("Por favor ingresa un numero: "))
print(f"{num1} es mayor que {num2}" * (num1 > num2) or f"{num1} es menor que {num2}" * (num1 < num2))