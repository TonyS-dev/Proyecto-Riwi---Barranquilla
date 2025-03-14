



try:
    nombre = input("Por favor ingrese el nombre del producto: ") 
    print("Nombre ingresado correctamente")
except ValueError:
    print("Nombre incorrecto")
try:
    precio_unitario = float(input("Por favor ingrese el valor del producto: "))
    if precio_unitario > 0:
        print("Producto ingresado correctamente")
    else:
        print("El precio tiene que ser mayor a 0")
except ValueError:
    print("Ingrese un valido")
            





            
            # if is_integer and value != int(value):
            #     print("*** El numero debe ser un entero. Intentalo de nuevo. ***")
            #     continue  #Regresa al inicio del ciclo
            
            # if value > 0:
            #     #Devuelve el valor como entero o flotante según se requiera
            #     if is_integer:
            #         return int(value)
            #     else:
            #         return value
            # else:
            #     print("*** El numero no puede ser negativo. Inténtalo de nuevo. ***")
        
            #Captura el error si la entrada no es un número válido
            
