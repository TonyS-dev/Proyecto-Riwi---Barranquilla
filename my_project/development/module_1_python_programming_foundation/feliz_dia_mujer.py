import turtle
import math
import random



screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Plano Cartesiano con Cuadrícula")

tortuga = turtle.Turtle()
tortuga.speed(0)  # Máxima velocidad


def dibujar_ejes():
    # Eje X (horizontal)
    tortuga.penup()
    tortuga.goto(-400, 0)
    tortuga.pendown()
    tortuga.goto(400, 0)
    tortuga.write("X", align="center", font=("Arial", 12, "bold"))

    # Eje Y (vertical)
    tortuga.penup()
    tortuga.goto(0, -400)
    tortuga.pendown()
    tortuga.goto(0, 400)
    tortuga.write("Y", align="center", font=("Arial", 12, "bold"))


def dibujar_cuadricula(espacio=50):
    tortuga.penup()
    tortuga.color("black")

    # Líneas verticales (eje X)
    for x in range(-400, 401, espacio):
        tortuga.goto(x, -400)
        tortuga.pendown()
        tortuga.goto(x, 400)
        tortuga.penup()
        if x != 0:  # Evitar escribir encima del eje Y
            tortuga.goto(x, 10)
            tortuga.write(str(x), align="center")

    # Líneas horizontales (eje Y)
    for y in range(-400, 401, espacio):
        tortuga.goto(-400, y)
        tortuga.pendown()
        tortuga.goto(400, y)
        tortuga.penup()
        if y != 0:  # Evitar escribir encima del eje X
            tortuga.goto(10, y)
            tortuga.write(str(y), align="left")


dibujar_ejes()
dibujar_cuadricula()



def imprimir_mensaje():
    # Mensaje para conmemorar el Día de la Mujer
    mensaje = """
    Hoy celebramos la fuerza, valentía y sabiduría de todas las mujeres del mundo.
    Gracias por su dedicación, amor y esfuerzo en cada paso que dan.
    Que nunca dejen de soñar, luchar y brillar.
    ¡Juntas son imparables!
    """
    return mensaje

def dibujar_corazon():
    # Configuración de la ventana
    ventana = turtle.Screen()
    ventana.bgcolor("#FFC5D3")
    ventana.title("Conmemoración del Día de la Mujer")
    
    # Crear una forma de corazón personalizada
    def mini_corazon():
        t = turtle.Turtle()
        t.hideturtle()
        ventana.tracer(0)
        
        t.penup()
        t.begin_poly()
        for ang in range(360):
            rad = math.radians(ang)
            x = 16 * math.sin(rad) ** 3
            y = 13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad)
            t.goto(x * 0.5, y * 0.5)
        t.end_poly()
        
        forma_corazon = t.get_poly()
        ventana.register_shape("mini_corazon", forma_corazon)
        ventana.tracer(1)
    
    mini_corazon()
    
    # Configuración de la tortuga principal
    tortuga = turtle.Turtle()
    tortuga.shape("mini_corazon")
    tortuga.color("red")
    tortuga.speed(0)
    tortuga.setheading(90)
    
    def dibujar_corazon_parametrico():
        tortuga.penup()
        inicio = 1
        theta = math.radians(inicio)
        x = 16 * math.sin(theta) ** 3
        y = 13 * math.cos(theta) - 5 * math.cos(2*theta) - 2 * math.cos(3*theta) - math.cos(4*theta)
        scale = 10
        tortuga.goto(x * scale, y * scale + 140)
        
        tortuga.pensize(4)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.color("red")
        
        for t in range(inicio, 360 + inicio, 1):
            theta = math.radians(t)
            x = 16 * math.sin(theta) ** 3
            y = 13 * math.cos(theta) - 5 * math.cos(2*theta) - 2 * math.cos(3*theta) - math.cos(4*theta)
            tortuga.goto(x * scale, y * scale + 140)
        
        tortuga.end_fill()
    
    dibujar_corazon_parametrico()
    
    tortuga.pensize(1)
    
    # Texto principal
    tortuga.penup()
    tortuga.goto(-200, -130)
    tortuga.pendown()
    tortuga.color("purple")
    tortuga.write("¡Feliz Día de la Mujer! 🌸", font=("Arial", 24, "bold"))
    
    # Función mejorada para dibujar estrellas con diseño más orgánico
    def dibujar_estrella_personalizada(x, y, size, color):
        tortuga.penup()
        tortuga.goto(x, y)
        tortuga.pendown()
        tortuga.color(color)
        tortuga.begin_fill()
        
        # Diseño de estrella más irregular
        for _ in range(5):
            tortuga.forward(size)
            tortuga.right(144)
            tortuga.forward(size * 0.6)  # Variación en la longitud de los brazos
            tortuga.left(70)
        
        tortuga.end_fill()
    
    # Dibujar estrellas con colores y diseños variados
    colores_estrellas = ["#FFD700", "#FF69B4", "#00FFFF", "#7CFC00", "#FF4500"]
    
    for _ in range(10):
        x = random.randint(-150, 150)
        y = random.randint(50, 250)
        size = random.randint(5, 20)
        color = random.choice(colores_estrellas)
        dibujar_estrella_personalizada(x, y, size, color)
    
    # Función para crear fuegos artificiales
    def fuegos_artificiales():
        for _ in range(5):
            # Crear tortuga de fuegos artificiales
            fuego = turtle.Turtle()
            fuego.hideturtle()
            fuego.speed(0)
            fuego.penup()
            
            # Posición aleatoria
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            
            # Color aleatorio
            color = random.choice(["#FF1493", "#00BFFF", "#32CD32", "#FF4500", "#9400D3"])
            fuego.color(color)
            
            # Dibujar explosión
            fuego.goto(x, y)
            fuego.pendown()
            fuego.begin_fill()
            
            # Crear forma de explosión
            for _ in range(36):
                fuego.forward(50)
                fuego.right(170)
            
            fuego.end_fill()
    
    # Llamar a fuegos artificiales
    fuegos_artificiales()
    
    # Mensaje completo
    tortuga.penup()
    tortuga.goto(-200, -230)
    tortuga.pendown()
    tortuga.color("purple")
    tortuga.write(imprimir_mensaje(), font=("Arial", 12, "normal"))
    
    ventana.mainloop()

# Llamar a la función para dibujar el corazón
if __name__ == "__main__":
    dibujar_corazon()