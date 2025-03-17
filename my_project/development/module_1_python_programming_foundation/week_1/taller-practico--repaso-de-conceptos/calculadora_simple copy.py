# Calificación de un estudiante
# ● Descripción: Escribe un programa que pida al usuario una calificación (número entre 0 y 
# 10). Luego, categoriza las calificaciones según el siguiente rango: Las calificaciones 9 a 10 
# se asociarán a la letra A, las calificaciones del 7 a 8.9 se asociarán a la letra B,  las 
# calificaciones del 5 a 6.9 quedarán asociadas a la letra C y por último si la calificación es 
# menor a 5 se le asignará la letra F



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