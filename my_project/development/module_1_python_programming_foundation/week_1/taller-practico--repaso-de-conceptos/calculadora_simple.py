# Descripción: Solicita dos números al usuario y muestra la suma, resta, multiplicación y división de ambos.
# • Requisito: Verificar si el divisor no es 0 antes de realizar la división.

num1 = int(input("Por favor ingresa un numero: "))
num2 = int(input("Por favor ingresa un numero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
es_divisble = num2 != 0
print(f"""
    Operaciones para {num1} y {num2} :
    Suma: {num1} + {num2} es igual a: {suma}
    Resta: {num1} - {num2} es igual a: {resta}
    Multiplicacion: {num1} * {num2} es igual a: {multiplicacion}
    """
    f"Division: no es posible dividir entre 0" * (not es_divisble) or f"Division: {num1} / {num2} es igual a: {num1 / num2}" * (es_divisble)
      )