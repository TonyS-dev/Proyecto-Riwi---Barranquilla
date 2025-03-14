#Pide al usuario su edad y muestra un mensaje que diga si su edad es mayor que 18 (usar operadores de comparación, sin condicionales).
edad = int(input("Por favor, ingresa tu edad: "))
print(f"Tienes {edad} años, Eres mayor de edad" * (edad >= 18) or f"Tienes {edad} años, Eres menor de edad" * (edad < 18))


