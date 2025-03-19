def control_notas(message):
    global lista_notas
    while True:
        # Solicitar entrada al usuario
        entrada = input(message)
        
        try:
            # Caso especial: verificar si es un solo número
            if "," not in entrada:
                # El usuario ingresó un solo valor
                print("Por favor ingresa al menos dos calificaciones separadas por comas.")
                continue
                
            # Procesar entrada normal con comas
            valores = [valor.strip() for valor in entrada.split(',') if valor.strip()]

            if len(valores) < 2:
                print("Por favor ingresa al menos dos calificaciones válidas.")
                continue
                
            lista_notas = [float(valor) for valor in valores]
            
            # Verificar que todos estén en rango
            if any(nota < 0 or nota > 100 for nota in lista_notas):
                print("Por favor ingresa notas entre 0 y 100")
                continue
                
            return lista_notas
                
        except ValueError:
            print("\n*** Cantidad inválida. Ingresa números válidos. ***")

def show_menu():
    global salir
    print(f"\nLista de notas actuales: {lista_notas}")

    print("""  Qué desea hacer? 
    1: Ingresar una nueva lista de notas
    2: Calcular promedio
    3: Comparar notas mayor qué
    4: Buscar frecuencia de una calificación especifica
    5: Salir""")
    
    option = input()
    if option in ("1"): control_notas("Por favor ingresa la nueva lista de notas (separadas por comas): ")
    elif option in ("2"): calcular_promedio() 
    elif option in ("3"): comparar_valor()
    elif option in ("4"): buscar_frecuencia()
    elif option in ("5"): print("Saliendo..."); salir = True ; return salir
    else: print('*** Respuesta invalida. Debes responder de "1" a "5". ***')

def calcular_promedio():
    print(f"{'*' * 40}")
    print(f"De las notas: {lista_notas}")
    print(f"El promedio es: ", sum(lista_notas) / len(lista_notas))
    print(f"{'*' * 40}")
    continuar()

def comparar_valor():
    valor_comparativo = float(input("Ingrese un valor para comparar que notas son mayores a él: "))
    notas_mayores = []
    for nota in lista_notas:
        if nota > valor_comparativo:
            notas_mayores.append(nota)
    print(f"{'*' * 40}")
    print(f"De las notas: {lista_notas}")
    print(f"Las notas mayores a {valor_comparativo} son: {notas_mayores}")
    print(f"{'*' * 40}")
    continuar()

def buscar_frecuencia():
    print("4")

def continuar():
    global salir
    user_input = input("Desea continuar? (Si/No): ")
    if user_input.lower() in ["si", "s", "sí"]:
            print("°°° Continuando... °°°")
           
        #Verifica si la respuesta es negativa
    elif user_input.lower() in ["no", "n"]:
        print("°°° Finalizando programa... °°°")
        salir = True ; return salir
    
    else:
        #Mensaje de error si la respuesta no es reconocida
        print('*** Respuesta invalida. Debes responder "si" o "no". ***')

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

lista_notas = []
salir = False
control_notas("!!! Por favor ingresa las notas separadas por comas (,): ")
while True:
    show_menu()
    if salir:
        break
        