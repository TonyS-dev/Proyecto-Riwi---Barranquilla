num_factorial = int(input("Ingrese un numero para calcular su factorial: "))
total = 1
print(f"{num_factorial}! :")  
for i in range(num_factorial, 0, -1):
    print(f"{i} * ", end="")
    total = total * i
print(f"\b\b = {total}") 

