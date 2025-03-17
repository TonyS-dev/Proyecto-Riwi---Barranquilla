// Funciones auxiliares
Funcion esNumero <- validarNumero(valor)
    Definir esNumero Como Logico;
    esNumero <- Verdadero;
    // Verificamos si el valor es un número válido
    Si valor = "" Entonces
        esNumero <- Falso;
    FinSi
FinFuncion

// Función para calcular el perímetro de un cuadrado
Funcion perimetro <- calc_perimetro(lado)
    Definir perimetro Como Real;
    perimetro <- lado * 4;
FinFuncion

// Función para convertir Celsius a Fahrenheit
Funcion fahrenheit <- conv_temp(celsius)
    Definir fahrenheit Como Real;
    fahrenheit <- (celsius * 9 / 5) + 32;
FinFuncion

// Función principal para probar ejercicios
Funcion ejercicio <- probarEjercicios(x)
    Definir numEjercicio Como Entero;
    Definir ejercicio Como Cadena;
    
    Escribir "¿Qué ejercicio quieres realizar? [1,2,3,4,5]";
    Leer numEjercicio;
    
    // Validar que el número del ejercicio sea válido
    Mientras numEjercicio < 1 O numEjercicio > 5 Hacer
        Escribir "Error: Por favor ingresa un número entre 1 y 5.";
        Leer numEjercicio;
    FinMientras
    
    Segun numEjercicio Hacer
        1:
            Definir lado Como Real;
            Definir entradaValida Como Logico;
            Definir confirmaTexto Como Cadena;
            Definir confirmacion Como Logico;
            
            Escribir 'Hola!, Este ejercicio calcula el perímetro de un cuadrado';
            
            confirmacion <- Falso;
            Mientras confirmacion = Falso Hacer
                Escribir 'Por favor ingresa la medida del lado del cuadrado:';
                Leer lado;
                
                entradaValida <- validarNumero(ConvertirATexto(lado));
                
                Si entradaValida Entonces
                    Escribir 'El lado es: ', lado;
                    Escribir 'Es esto Verdadero o Falso?';
                    Leer confirmaTexto;
                    
                    Si Minusculas(confirmaTexto) = "verdadero" Entonces
                        confirmacion <- Verdadero;
                    SiNo
                        Si Minusculas(confirmaTexto) = "falso" Entonces
                            confirmacion <- Falso;
                        SiNo
                            Escribir 'Error: Ingresa Verdadero o Falso.';
                            confirmacion <- Falso;
                        FinSi
                    FinSi
                SiNo
                    Escribir 'Error: Ingresa un número válido.';
                FinSi
            FinMientras
            
            Escribir 'El perímetro es: ', calc_perimetro(lado);
            
        2:
            Definir celsius Como Real;
            Definir entradaValida Como Logico;
            Definir confirmaTexto Como Cadena;
            Definir confirmacion Como Logico;
            
            Escribir 'Hola!, Este ejercicio convierte la temperatura de grados Celsius a Fahrenheit';
            
            confirmacion <- Falso;
            Mientras confirmacion = Falso Hacer
                Escribir 'Por favor ingresa la temperatura en grados Celsius:';
                Leer celsius;
                
                entradaValida <- validarNumero(ConvertirATexto(celsius));
                
                Si entradaValida Entonces
                    Escribir 'La temperatura es: ', celsius, '° Celsius';
                    Escribir 'Es esto Verdadero o Falso?';
                    Leer confirmaTexto;
                    
                    Si Minusculas(confirmaTexto) = "verdadero" Entonces
                        confirmacion <- Verdadero;
                    SiNo
                        Si Minusculas(confirmaTexto) = "falso" Entonces
                            confirmacion <- Falso;
                        SiNo
                            Escribir 'Error: Ingresa Verdadero o Falso.';
                            confirmacion <- Falso;
                        FinSi
                    FinSi
                SiNo
                    Escribir 'Error: Ingresa un número válido.';
                FinSi
            FinMientras
            
            Escribir 'La temperatura en grados Fahrenheit es: ', conv_temp(celsius);
            
        3:
            Definir num1, num2 Como Real;
            Definir entradaValida Como Logico;
            
            Escribir 'Hola!, Este ejercicio calcula la suma entre dos números';
            
            Escribir 'Por favor ingresa un valor para el número 1: ';
            Leer num1;
            entradaValida <- validarNumero(ConvertirATexto(num1));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer num1;
                entradaValida <- validarNumero(ConvertirATexto(num1));
            FinMientras
            
            Escribir 'Por favor ingresa un valor para el número 2: ';
            Leer num2;
            entradaValida <- validarNumero(ConvertirATexto(num2));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer num2;
                entradaValida <- validarNumero(ConvertirATexto(num2));
            FinMientras
            
            Escribir 'La suma de los dos números es: ', num1 + num2;
            
        4:
            Definir nota1, nota2, nota3 Como Real;
            Definir entradaValida Como Logico;
            
            Escribir 'Hola!, Este ejercicio calcula el promedio de tres calificaciones';
            
            Escribir 'Por favor ingresa un valor para la nota 1: ';
            Leer nota1;
            entradaValida <- validarNumero(ConvertirATexto(nota1));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer nota1;
                entradaValida <- validarNumero(ConvertirATexto(nota1));
            FinMientras
            
            Escribir 'Por favor ingresa un valor para la nota 2: ';
            Leer nota2;
            entradaValida <- validarNumero(ConvertirATexto(nota2));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer nota2;
                entradaValida <- validarNumero(ConvertirATexto(nota2));
            FinMientras
            
            Escribir 'Por favor ingresa un valor para la nota 3: ';
            Leer nota3;
            entradaValida <- validarNumero(ConvertirATexto(nota3));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer nota3;
                entradaValida <- validarNumero(ConvertirATexto(nota3));
            FinMientras
            
            Escribir 'El promedio de las notas es: ', (nota1 + nota2 + nota3) / 3;
            
        5:
            Definir edad Como Entero;
            Definir entradaValida Como Logico;
            
            Escribir 'Hola!, Este ejercicio determina si una persona es mayor de edad';
            
            Escribir 'Por favor ingresa tu edad: ';
            Leer edad;
            entradaValida <- validarNumero(ConvertirATexto(edad));
            
            Mientras NO entradaValida Hacer
                Escribir 'Error: Ingresa un número válido.';
                Leer edad;
                entradaValida <- validarNumero(ConvertirATexto(edad));
            FinMientras
            
            Si edad >= 18 Entonces
                Escribir 'Eres mayor de edad';
            SiNo
                Escribir 'Eres menor de edad';
            FinSi
    FinSegun
    
    ejercicio <- "Ejercicio completado";
FinFuncion

// Algoritmo principal
Algoritmo admin_ejercicios
    Definir respuesta Como Cadena;
    respuesta <- 'si'; // Inicializar para entrar al bucle
	
    Mientras respuesta = 'si' Hacer
        Escribir probarEjercicios(0); // El valor de x no se usa en este caso
        Escribir '¿Quieres volver a ver/realizar los ejercicios? [Si/No]';
        Leer respuesta;
        respuesta <- Minusculas(respuesta);
		
        // Validar que la respuesta sea "si" o "no"
        Mientras respuesta <> 'si' Y respuesta <> 'no' Hacer
            Escribir 'Error: Ingresa si o no.';
            Leer respuesta;
            respuesta <- Minusculas(respuesta);
        FinMientras
    FinMientras
	
    Escribir 'Fin del programa.';
FinAlgoritmo