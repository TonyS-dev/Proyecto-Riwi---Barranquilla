# Dada una lista de números enteros, escribe un programa que recorra la lista con un ciclo while. Si 
# un número es par, imprímelo.  
numeros = (1, 2, 3, 4, 5, 6)

for numero in numeros:
    while numero % 2 == 0:
        print(f"{numero} es par")
        break