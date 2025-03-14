#Pide al usuario dos números y muestra si el primero NO es igual al segundo (usar operador lógico not combinado con comparación).
num1 = int(input("Por favor ingresa un numero: "))
num2 = int(input("Por favor ingresa un numero: "))
print(f"{num1} no es igual a {num2}" * (not num1 == num2) or f"Ambos numeros son iguales" * (not num1 != num2))