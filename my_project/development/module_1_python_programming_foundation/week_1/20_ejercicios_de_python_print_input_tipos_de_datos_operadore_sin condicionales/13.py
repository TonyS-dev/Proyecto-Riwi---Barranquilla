#Pide al usuario dos números enteros y muestra si son iguales (usar operadores de comparación, sin condicionales).
num1 = int(input("Por favor ingresa un numero: "))
num2 = int(input("Por favor ingresa un numero: "))
print("Los numeros son iguales" * (num1 == num2) or "Los numeros no son iguales" * (num1 != num2))