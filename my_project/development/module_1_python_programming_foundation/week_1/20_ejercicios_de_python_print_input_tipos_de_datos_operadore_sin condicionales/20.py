#Pide al usuario un número entero y muestra si el número es divisible entre 5 (usar operador de módulo % y comparación).
num1 = int(input("Por favor ingresa un numero entero: "))
print(f"{num1} es divisible entre 5" * (num1 % 5 == 0) or f"{num1} no es divisible entre 5" * (num1 % 5 != 0))
