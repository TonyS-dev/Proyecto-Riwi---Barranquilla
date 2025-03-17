# Dada tupla donde contiene el nombre, apellido de una persona y su edad. Escribe un programa
# que recorra la lista usando un ciclo for. Si la edad de la persona es menor de 18 años, omítela
# utilizando continue. Si la edad es mayor de 60, detén el ciclo utilizando break y muestra un
# mensaje indicando que se encontró una persona mayor de 60 años

persona = ("jose", "martinez", "55")

for dato in persona:
    try:
        edad = int(dato)
        if edad < 18:
            continue
        elif edad > 60:
            print("Persona mayor de 60 años encontrada")
            break
    except:
        continue