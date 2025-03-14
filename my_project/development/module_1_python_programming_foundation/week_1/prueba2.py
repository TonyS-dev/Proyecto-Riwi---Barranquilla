def control_numeros(mensaje, tipo=float, valor_minimo=0, valor_maximo=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor <= valor_minimo:
                print(f"El valor debe ser mayor a {valor_minimo}")
                continue
            if valor_maximo and valor > valor_maximo:
                print(f"El valor debe ser menor o igual a {valor_maximo}")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Intente nuevamente.")

def solicitar_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).lower()
        if opcion in opciones_validas:
            return opcion
        print("Opción inválida.")

print (f"Hola, bienvenidos a su tienda en línea. Por favor, escriba los siguientes datos:")

nombre_del_producto = input("Por favor escriba el nombre del producto: ")
precio_unitario = control_numeros("Por favor mencione el valor del producto: ")
cantidad = control_numeros("Por favor mencione la cantidad del producto: ", tipo=int)
con_descuento = solicitar_opcion("Desea aplicar descuento? si(s) - no(n) ", ["s", "n", "si", "no"])
porcentaje_descuento = 0
if con_descuento == "s" or con_descuento == "si":
    porcentaje_descuento = control_numeros("Por favor indique del porcentaje del descuento: ", tipo=int, valor_minimo=0, valor_maximo=100)

total_sin_descuento = precio_unitario * cantidad
total_con_descuento = total_sin_descuento * (porcentaje_descuento / 100)
total_final = total_sin_descuento - total_con_descuento

print(f""" -----FACTURA------\n \n El nombre del producto es: {nombre_del_producto} \n Cantidad del producto es: {cantidad} \n Valor unitario del producto: {precio_unitario:.2f} \n Total sin descuento es: {total_sin_descuento:.2f} \n Total con descuento es: {total_final:.2f} \n Gracias por su compra. Vuelva pronto.""")
