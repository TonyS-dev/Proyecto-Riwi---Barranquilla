#Función para manejar y verificar correctamente todas las entradas númericas, sean int o float
def handle_number_inputs(message, is_integer=False):
    #Ciclo infinito que se ejecuta hasta que se ingrese un valor válido
    while True:
        try:
            #Intenta convertir la entrada del usuario a un número flotante
            value = float(input(message))
            
            #Verifica si el valor debe ser entero y si tiene decimales
            if is_integer and value != int(value):
                print("*** El numero debe ser un entero. Intentalo de nuevo. ***")
                continue  #Regresa al inicio del ciclo
            
            #Verifica que el valor no sea negativo
            if value >= 0:
                #Devuelve el valor como entero o flotante según se requiera
                if is_integer:
                    return int(value)
                else:
                    return value
            else:
                print("*** El numero no puede ser negativo. Inténtalo de nuevo. ***")
        except ValueError:
            #Captura el error si la entrada no es un número válido
            print("*** Cantidad invalida. Ingresa un numero valido. ***")

#Función para manejar y verificar correctamente la asignación de descuento
def handle_discounts(message):
    #Ciclo infinito que se ejecuta hasta obtener una respuesta válida sobre aplicar descuento
    while True:
        #Solicita al usuario que indique si aplicará un descuento
        user_input = input("--- Existe algun descuento? (si/no): ")
        
        #Verifica si la respuesta es afirmativa (aceptando diferentes variaciones)
        if user_input.lower() in ["si", "s", "sí"]:
            print("°°° Continuando... °°°")
            
            #Ciclo para obtener un valor de descuento válido
            while True:
                try:
                    #Intenta convertir la entrada a un entero
                    value = int(input(message))
                    
                    #Verifica que el descuento esté en el rango válido (1-99)
                    if value > 0 and value < 100:
                        print("==>> Descuento correctamente asignado.")
                        return value
                    else:
                        print("*** El descuento tiene que ser de 1 a 99 por ciento. Inténtalo de nuevo. ***")
                except ValueError:
                    #Captura el error si la entrada no es un número válido
                    print("*** Cantidad invalida. Ingresa un numero valido. ***")
        
        #Verifica si la respuesta es negativa
        elif user_input.lower() in ["no", "n"]:
            print("°°° Finalizando... Descuento no asignado °°°")
            #Asigna 0 como valor de descuento si no se aplica ninguno
            value = 0
            return value
        else:
            #Mensaje de error si la respuesta no es reconocida
            print('*** Respuesta invalida. Debes responder "si" o "no". ***')

# ----- PROGRAMA PRINCIPAL -----
#
# Programa para gestionar la compra de multiples productos con descuentos
# Este sistema permite al usuario ingresar diferentes productos
# Calcula el precio sub-total, total y aplica descuentos segun las preferencias
#

#Solicitud de la cantidad de productos a ingresar
cantidad_productos = handle_number_inputs("!!! Por favor ingresa la cantidad de productos: ", is_integer=True)
print("/// Cantidad de productos correctamente ingresada. ///")

#Inicialización de variables para almacenar productos y precio total
precio_total = 0
productos = []

#Ciclo para solicitar la información de cada producto
for i in range(cantidad_productos):
    #Creación de diccionario para almacenar información de cada producto
    producto = {
        "nombre": input(f"!!! Por favor ingresa el nombre del producto {i + 1}: "),
        "precio": handle_number_inputs(f"!!! Por favor ingresa el precio del producto {i + 1}: ")
    }
    #Agregando el producto a la lista y actualizando el precio total
    productos.append(producto)
    precio_total += producto["precio"]  #Acumulación del precio en el total
    print("/// Precio de producto correctamente ingresado. ///")

print("/// Productos ingresados correctamente ///")

#Asignación para manejar el descuento que se va a aplicar
descuento_producto = handle_discounts("°°° Procediendo con descuentos... ingresa el descuento (1-99): ")

#Asignación para el precio final de los productos con descuento aplicado, utilizando la formula basica de descuentos
precio_con_descuento = precio_total - (precio_total * (descuento_producto / 100))

#Impresión con formatos adecuados del resumen de:
# 1. La cantidad de productos
# 2. Listado de productos
# 3. Precio sub-total de todos los produtos
# 4. Descuento asignado a todos los productos
# 5. Precio final con descuentos aplicados (si aplica)
print("\n------------- ORDEN DETALLES -------------")
print(f"Numero de productos: #{cantidad_productos}")

#Listado detallado de cada producto ingresado
print("\n----------- LISTA DE PRODUCTOS -----------")
for producto in productos:
    print(f"{producto["nombre"]}: ${producto["precio"]:.2f}")
print("------------------------------------------")

#Sección para mostrar los precios
print(f"Precio sub-total: ${precio_total:.2f}")
print(f"Descuento seleccionado: {descuento_producto}%")
print(f"Precio total: ${precio_con_descuento:.2f}")
print("------------------------------------------")