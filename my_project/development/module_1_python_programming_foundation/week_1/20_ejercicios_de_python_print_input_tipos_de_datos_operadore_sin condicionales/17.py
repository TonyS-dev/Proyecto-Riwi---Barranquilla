#Pide al usuario dos números y muestra si al menos uno es mayor que 10 (usar operador lógico or).
num1 = int(input("Por favor ingresa un numero: "))
num2 = int(input("Por favor ingresa un numero: "))
print(f"Al menos un numero es mayor que 10" * (num1 > 10 or num2 > 10) or f"Ningún numero es mayor que 10" * (num1 <= 10 and num2 <= 10))