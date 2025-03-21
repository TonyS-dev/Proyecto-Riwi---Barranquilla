# TAREAS
# ✅ Verificar que en todo momento los datos ingresados son validos.
# ✅ Pedir al usuario que ingrese en un solo input, una lista de notas (de 0 a 100), separadas por comas.
# ✅ Convertir el input en una lista de numeros, para poder ejecutar las operaciones matematicas.
# ✅ Solicitar y validar la calificación mínima aprobatoria
# ✅ Calcular el promedio de todas las calificaciones y determinar si el usuario aprobó, (en base a la calificacion minima aprobatoria ingresada)
# ✅ Preguntar al usuario por un valor comparativo, y determinar cuantas calificaciones son mayores que este valor.
# ✅ Solicitar una calificación específica a buscar para verificar y contar cuántas veces aparece esa calificación específica
# ✅ Mostrar todos los resultados de manera clara y organizada

from os import system #Importacion para mostrar posteriormente la consola de una manera limpia

def mostrar_menu(): #Función para mostrar el menu infinitamente durante la ejecución del programa
    global salir #Declaramos la variable global, para que funcione como un switch(on/off) que permite finalizar el programa
    print(f"\nLista de notas actuales: {lista_notas}")

    print("""  Qué desea hacer? 
    0: Ingresar una nueva lista de notas
    1: Determinar el estado de aprobación
    2: Calcular promedio
    3: Contar calificaciones mayores
    4: Verificar y contar calificaciones específicas
    5: Salir""")
    #Utilizo un menu, debido a que es más comodo ir mostrando todas las funcionalidades que tiene el programa de manera interactiva
    option = input()
    if option in ("0"): control_notas("Por favor ingresa la nueva lista de notas (separadas por comas): ") 
    elif option in ("1"): determinar_aprobacion()
    elif option in ("2"): calcular_promedio() 
    elif option in ("3"): comparar_valor()
    elif option in ("4"): buscar_frecuencia()
    elif option in ("5"): print("Saliendo..."); salir = True ; return salir #permite la finalización del bucle infinito
    else: print('*** Respuesta invalida. Debes responder de "0" a "5". ***')

def control_numeros(message):
    while True: #Ciclo infinito que se ejecuta hasta que se ingrese un valor válido
        try:
            valor = float(input(message)) #Intenta convertir la entrada del usuario a un número flotante
            
            if valor >= 0 and valor <= 100: #Verifica que el valor este entre (incluyendo) 0 y 100
                return valor
            else:
                print("*** Por favor ingresa notas entre 0 y 100. Inténtalo de nuevo. ***")
                
        except ValueError: #Captura el error si la entrada no es un número válido
            print("*** Cantidad invalida. Ingresa un numero valido. ***")

def control_notas(message):
    global lista_notas
    while True:
        # Solicita input al usuario
        entrada = input(message)    
        try:
            if "," not in entrada: # Caso especial: verifica si el input es un solo numero o si no tiene comas
                print("Por favor ingresa al menos dos calificaciones separadas por comas.")
                continue
                
            # por cada valor en la entrada separada por comas, si no tiene espacios, asignamos cada valor a una lista llamada valores [] y a su vez le eliminamos los espacios con strip() a cada valor
            valores = [valor.strip() for valor in entrada.split(',') if valor.strip()]
            # valido que la lista sea mayor que 1
            if len(valores) < 2:
                print("Por favor ingresa al menos dos calificaciones válidas.")
                continue #ejecutamos nuevamente todo este bloque de while
            # a cada valor en la lista valores lo transformo en float, si esto falla, el except value error salta    
            lista_notas = [float(valor) for valor in valores]
            
            if any(nota < 0 or nota > 100 for nota in lista_notas): # (gracias al uso de any) Verificar que TODAS las notas estén en rango
                print("Por favor ingresa notas entre 0 y 100")
                continue #ejecutamos nuevamente todo este bloque de while
            return lista_notas
                
        except ValueError:
            print("\n*** Cantidad inválida. Ingresa números válidos. ***")

def determinar_aprobacion(): #yo utilizo "str" * (calificacion > calificacion_minima) or ... en lugar de if,elif,else, debido a que permite eficientemente imprimir el texto correspondiente a la expresion que sea verdadera, en una sola linea.
    calificacion_minima = control_numeros("Ingresa una calificación MINIMA de 0 a 100: ")
    calificacion = control_numeros("Ingresa una calificacion a comparar: ")
    print(f"{'*' * 40}")
    print(f"De la nota: {calificacion} y la calificación minima {calificacion_minima}")
    print(f"!!!Aprobaste, felicidades!!!" * (calificacion > calificacion_minima) or f"No aprobaste :(" * (calificacion < calificacion_minima))
    print(f"{'*' * 40}")
    continuar()

def calcular_promedio(): #yo utilizo el metodo sum en lugar de for, porque me permite sumar todos los datos en lista_notas, en una sola linea de manera eficiente calculando el promedio
    valor_minimo = control_numeros("Ingrese el valor minimo aprobatorio: ")
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"{'*' * 40}")
    print(f"De las notas: {lista_notas}")
    print(f"El promedio es: {promedio}")
    print(f"Del valor minimo aprobatorio {valor_minimo}: ")
    print(f"\n    !!!Felicidades aprobaste!!!" * (promedio > valor_minimo) or f"No aprobaste :(" * (promedio < valor_minimo))
    print(f"{'*' * 40}")
    continuar()

def comparar_valor(): #yo utilizo un ciclo for en lugar de while, para iterar y procesar cada nota en lista_notas, ya que me pemite llevar un mayor control, sobre la iteracion actual y la finalizacion de todo el bucle, en menos lineas de codigo.
    valor_comparativo = control_numeros("Ingrese un valor para comparar que notas son mayores a él: ")
    notas_mayores = []
    for nota in lista_notas:
        if nota > valor_comparativo:
            notas_mayores.append(nota)
    print(f"{'*' * 40}")
    print(f"De las notas: {lista_notas}")
    print(f"Se encontraron {len(notas_mayores)} notas mayor(es) \nLas notas mayores a {valor_comparativo} son: {notas_mayores}" * (len(notas_mayores) > 0) or f"No existen notas mayores a {valor_comparativo}" * (len(notas_mayores) < 1))
    print(f"{'*' * 40}")
    continuar()

def buscar_frecuencia(): #utilizo for para verificar cada nota, y verificar si es identica a la nota a buscar
    nota_a_buscar = control_numeros("Por favor ingrese el valor a buscar dentro de las calificaciones: ")
    notas_cantidad = 0
    for nota in lista_notas:
        if nota == nota_a_buscar:
            notas_cantidad += 1
    print(f"{'*' * 40}")
    print(f"De las notas: {lista_notas}")
    print(f"Se encontraron {notas_cantidad} nota(s) similares" * (notas_cantidad > 0) or f"No existen notas similares" * (notas_cantidad < 1))
    print(f"{'*' * 40}")
    continuar()

def continuar(): #funcion para ejecutar una vez finalice cada opcion o particularidad del programa, permite continuar o finalizar el programa
    global salir #nuevamente uso global porque tambien podemos salir o detener el programa desde la funcion continue
    user_input = input("Desea continuar? (Si/No): ")
    if user_input.lower() in ["si", "s", "sí"]:
            print("°°° Continuando... °°°") #Debido a que mostrar_menu () está en un while true, siempre se ejecutará. 
                                            #Por lo que se espera que se muestre y no es necesario llamar nuevamente mostrar menu aqui.

    elif user_input.lower() in ["no", "n"]: #Verifica si la respuesta es negativa sea mayuscula o minuscula
        print("°°° Finalizando programa... °°°")
        salir = True ; return salir
    
    else:
        print('*** Respuesta invalida. Debes responder "si" o "no". ***') #Mensaje de error si la respuesta no es reconocida

# ----- PROGRAMA PRINCIPAL -----
#
# Programa para gestionar el ingreso de notas dinamicas y el calculo de operaciones estadisticas
# Este sistema permite al usuario ingresar listas de numeros separadas por comas continuamente
# Calcula el promedio, la frecuencia de una nota y la comparación de una nota en especifico
#

system("clear") #limpiamos la consola cada vez que ejecutamos el programa
lista_notas = [] #declaramos globalmente salir y lista_notas
salir = False
print("Bienvenido a este programa para gestionar el ingreso de notas dinamicas".title()) #mensaje de bienvenida
control_notas("!!! Por favor ingresa las notas separadas por comas (,): ") #siempre preguntar por lista notas, cada vez que inicia el programa 
while True: #bucle infinito para manejar la interactividad del programa
    mostrar_menu()
    if salir: #si asiganamos valor a la variable salir desde la funcion mostrar menu o continue, esta condicion se aplicara y ejecutara el break, rompiendo el ciclo infinito
        break