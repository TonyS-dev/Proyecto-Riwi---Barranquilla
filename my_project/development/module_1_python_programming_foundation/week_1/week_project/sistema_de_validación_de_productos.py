#Función para manejar y verificar correctamente todas las entradas númericas, sean int o float
def handle_number_inputs(message, is_integer=False):
    while True:
        try:
            value = float(input(message))
            if is_integer and value != int(value):
                print("*** El numero debe ser un entero. Intentalo de nuevo. ***")
                continue
            if value >= 0:
                return int(value) if is_integer else value
            else:
                print("*** El numero no puede ser negativo. Inténtalo de nuevo. ***")
        except ValueError:
            print("*** Cantidad invalida. Ingresa un numero valido. ***")


#Función para manejar y verificar correctamente la asignación de descuento
def handle_discounts(message):
    while True:
        user_input = input("--- Existe algun descuento? (si/no): ")
        if user_input.lower() in ["si", "s", "sí"]:
            print("°°° Continuando... °°°")
            while True:
                try:
                    value = int(input(message))
                    if value > 0 and value < 100:
                        print("==>> Descuento correctamente asignado.")
                        return value
                    else:
                        print("*** El descuento tiene que ser de 1 a 99 por ciento. Inténtalo de nuevo. ***")
                except ValueError:
                    print("*** Cantidad invalida. Ingresa un numero valido. ***")
        elif user_input.lower() in ["no", "n"]:
            print("°°° Finalizando... Descuento no asignado °°°")
            value = 0
            return value
        else:
            print("*** Respuesta invalida. Debes responder 'si' o 'no'. ***")

# -----
#
#
#
#
cantidad_productos = handle_number_inputs("!!! Por favor ingresa la cantidad de productos: ", is_integer=True)
print("/// Cantidad de productos correctamente ingresada. ///")

precio_total = 0
for i in range(cantidad_productos):
    nombre_producto = input(f"!!! Por favor ingresa el nombre del producto {i + 1}: ")

    precio_unitario = handle_number_inputs(f"!!! Por favor ingresa el precio del producto {i + 1}: ")
    print("/// Precio de producto correctamente ingresado. ///")

    precio_total = precio_total + precio_unitario

print("/// Productos ingresados correctamente ///")


#Asignación para manejar el descuento que se va a aplicar
descuento_producto = handle_discounts("°°° Procediendo con descuentos... ingresa el descuento (1-99): ")


#Asignación para el precio final de los productos con descuento aplicado, utilizando la formula basica de descuentos
precio_con_descuento = (precio_total - (precio_total * (descuento_producto / 100))) 


#Impresión con formatos adecuados del resumen de:
# 1. La cantidad de productos 
# 2. Precio total de todos los produtos
# 3. Descuento asignado a todos los productos
# 4. Precio final con descuentos aplicados

print("------------------------------ ORDEN DETALLES ------------------------------")
print(f"Numero de productos: #{cantidad_productos}")
print(f"Precio sub-total: ${precio_total:.2f}")
print(f"Descuento seleccionado: {descuento_producto}%")
print(f"Precio total con descuento: ${precio_con_descuento:.2f}")