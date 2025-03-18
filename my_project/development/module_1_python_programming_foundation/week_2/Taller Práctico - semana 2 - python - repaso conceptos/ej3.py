# Crea un programa que reciba una lista de números enteros y utilice un ciclo while para recorrerlos. 
# Si se encuentra un número negativo, se debe imprimir un mensaje y detener el ciclo utilizando la 
# instrucción break. Si el número es mayor que 100, se debe continuar con el siguiente número 
# utilizando continue. Al final, debe imprimir la cantidad de números procesados que son mayores 
# que 50. 

numeros = []
mayores_50 = 0
numeros_mayores_50 = []
i = 0
cantidad_numeros = int(input("Cuantos numeros desea ingresar?: "))

for x in range(1, cantidad_numeros + 1):
    numeros.append(int(input(f"Por favor ingrese el numero {x}: ")))

print("\n")

while i < len(numeros):
    
    if numeros[i] < 0:    
        print(f"{numeros[i]} es un numero negativo, deteniendo programa...")
        break

    elif numeros[i] > 100: 
        print(f"{numeros[i]} es mayor que 100 y que 50")
        mayores_50 += 1
        numeros_mayores_50.append(numeros[i])
        i += 1
        continue

    if numeros[i] > 50:
        mayores_50 += 1
        numeros_mayores_50.append(numeros[i])
        print(f"{numeros[i]} es mayor que 50 pero menor que 100")

    i += 1
    
print(f"\nHubo {mayores_50} numero(s) mayores que 50")
print(f"Son los siguientes: {numeros_mayores_50}")