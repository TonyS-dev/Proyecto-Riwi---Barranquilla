#Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.

num1 = float(input("Por favor ingresa un numero: "))
num2 = float(input("Por favor ingresa un numero: "))

modulo = num1 % num2
resultado_division_entera = num1 // num2
print(f"La división entre {num1} y {num2} tiene como resultado: {resultado_division_entera} y su modulo es: {modulo}")
