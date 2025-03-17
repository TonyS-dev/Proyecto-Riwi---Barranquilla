# Crea un programa que reciba una lista de números enteros y utilice un ciclo while para recorrerlos. 
# Si se encuentra un número negativo, se debe imprimir un mensaje y detener el ciclo utilizando la 
# instrucción break. Si el número es mayor que 100, se debe continuar con el siguiente número 
# utilizando continue. Al final, debe imprimir la cantidad de números procesados que son mayores 
# que 50. 

numeros = (100, 225, 3, 445, -55, 60)

i = 0

while i < len(numeros) + 1:
    if numeros[i] > 100: 
        print(f"{numeros[i]} es mayor que 100")
        i += 1
        continue
    elif numeros[i] < 0:    
        print(f"{numeros[i]} es un numero negativo, deteniendo programa...")
        break

    if numeros[i] > 50:
        print(f"{numeros[i]} es mayor que 50")
    i += 1
