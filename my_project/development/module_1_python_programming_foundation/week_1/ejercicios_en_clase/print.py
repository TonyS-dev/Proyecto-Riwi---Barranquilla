nombre = input("!!! Por favor ingresa tu nombre: ")
apellido = input("!!! Por favor ingresa tu apellido: ")
edad = int(input("!!! Por favor ingresa tu edad: "))
altura = float(input("!!! Por favor ingresa tu altura: "))

respuesta = input("!!! Por favor indica si respiras bajo el agua (si/no): ").lower()
if respuesta == "si":
    respira_bajo_el_agua = True
    mensaje_respiracion = "respiras bajo el agua"
elif respuesta == "no":
    respira_bajo_el_agua = False
    mensaje_respiracion = "no respiras bajo el agua"
else:
    print("Respuesta no válida. Por favor responde 'si' o 'no'.")
    respira_bajo_el_agua = False  
    mensaje_respiracion = "no has especificado si respiras bajo el agua"

print(f"Te llamas {nombre} {apellido} tienes {edad} años, mides {altura}mts, y {mensaje_respiracion}")