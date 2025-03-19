#Función para manejar y verificar correctamente todas las entradas númericas, sean int o float
# def handle_number_inputs(message, is_integer=False):
#     #Ciclo infinito que se ejecuta hasta que se ingrese un valor válido
#     while True:
#         try:
#             #Intenta convertir la entrada del usuario a un número flotante
#             value = float(input(message))
            
#             #Verifica si el valor debe ser entero y si tiene decimales
#             if is_integer and value != int(value):
#                 print("\n*** El numero no puede ser decimal. Intentalo de nuevo. ***")
#                 continue  #Regresa al inicio del ciclo
            
#             #Verifica que el valor no sea negativo
#             if value >= 0:
#                 #Devuelve el valor como entero o flotante según se requiera
#                 if is_integer:
#                     return int(value)
#                 else:
#                     return value
#             else:
#                 print("\n*** El numero no puede ser negativo. Inténtalo de nuevo. ***")
#         except ValueError:
#             #Captura el error si la entrada no es un número válido
#             print("\n*** Cantidad invalida. Ingresa un numero valido. ***")

def handle_grade_list(message):
    global lista_notas
    while True:
        try:
            #
            values = input(message)

            if values.find(",") < 1 and values.find(" ") >= 1:
                print("Por favor utilice comas para separar las calificaciones ex: 25, 30")
                continue

            values = values.replace(" ","").split(",")
            
            lista_notas = [float(value) for value in values]
            if len(lista_notas) <= 1:
                print("Por favor ingresa más de una calificación")
                continue

            notas_validas = False
            for nota in lista_notas:
                if nota < 0 or nota > 100:
                    print("Por favor ingresa una nota entre 0 y 100")
                    notas_validas = False
                    break
                else:
                    notas_validas = True
            
            if notas_validas:
                return lista_notas
                
        except ValueError:
            #Captura el error si la entrada no es un número válido
            print("\n*** Cantidad invalida. Ingresa un numero valido. ***")

def show_menu():
    global salir
    print(f"\n\n\nLista de notas actuales: {lista_notas}")

    print("""\n Qué desea hacer? 
    1: Ingresar una nueva lista de notas
    2: Calcular promedio
    3: Comparar valor mayor a
    4: Buscar frecuencia de una calificación especifica
    
    5: Salir""")
    
    option = input()
    if option in ("1"): handle_grade_list("Por favor ingresa la nueva lista de notas (separads por comas): ")
    elif option in ("2"): calcular_promedio() 
    elif option in ("3"): comparar_valor()
    elif option in ("4"): buscar_frecuencia()
    elif option in ("5"): print("Saliendo..."); salir = True ; return salir
    else: print('*** Respuesta invalida. Debes responder de "1" a "5". ***')

def calcular_promedio():
    print("2")

def comparar_valor():
    print("3")


def buscar_frecuencia():
    print("4")


# ----- PROGRAMA PRINCIPAL -----
#
# Programa para gestionar la compra de multiples productos con cantidades y descuentos
# Este sistema permite al usuario ingresar diferentes productos con sus cantidades
# Calcula el precio sub-total, total y aplica descuentos segun las preferencias
#

# ✅ Verificar que en todo momento los datos ingresados son validos.
# ✅ Pedir al usuario que ingrese en un solo input, una lista de notas (de 0 a 100), separadas por comas.
# ✅ Convertir el input en una lista de numeros, para poder ejecutar las operaciones matematicas.
# ✅ Solicitar y validar la calificación mínima aprobatoria
# ✅ Calcular el promedio de todas las calificaciones y determinar si el usuario aprobó, (en base a la calificacion minima aprobatoria ingresada)
# ✅ Preguntar al usuario por un valor comparativo, y determinar cuantas calificaciones son mayores que este valor.
# ✅ Solicitar una calificación específica a buscar para verificar y contar cuántas veces aparece esa calificación específica
# ✅ Mostrar todos los resultados de manera clara y organizada

# lista_notas = handle_grade_list("!!! Por favor ingresa la lista de notas separadas por comas (,): ")
# print("\nNotas ingresadas correctamente, son las siguientes: ")
# print(lista_notas)
lista_notas = []
while True:
    show_menu()
    if salir:
        break
        