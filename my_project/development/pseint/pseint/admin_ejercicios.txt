Función perimetro <- calc_perimetro (lado)
perimetro <- lado*4;
FinFunción

Función fahrenheit <- conv_temp (celsius)
fahrenheit <- (celsius*9/5)+32;
FinFunción

Función ejercicio <- probarEjercicios (x)
	Escribir "Qué ejercicio quieres realizar? [1,2,3,4,5]";
	Leer numEjercicio
	Segun numEjercicio Hacer
		1:
			Definir lado Como Entero;
			Escribir 'Hola!, Este ejercicio calcula el perímetro de un cuadrado';
			Definir confirmacion Como Lógico;
			Mientras confirmacion==Falso Hacer
				Escribir 'Por favor ingresa la medida del lado del cuadrado:';
				Leer lado;
				Escribir 'El lado es: ', lado;
				Escribir 'Es esto Verdadero o Falso?';
				Leer confirmacion;
			FinMientras
			Escribir 'El perímetro es: ', calc_perimetro(lado);
		2:
			Definir celsius Como Entero;
			Escribir 'Hola!, Este ejercicio convierte la temperatura de grados Celsius a Fahrenheit';
			Definir confirmacion Como Lógico;
			Mientras confirmacion==Falso Hacer
				Escribir 'Por favor ingresa la temperatura en grados Celsius:';
				Leer celsius;
				Escribir 'La temperatura es: ', celsius,'° Celsius';
				Escribir 'Es esto Verdadero o Falso?';
				Leer confirmacion;
			FinMientras
			Escribir 'La temperatura en grados Fahrenheit es: ', conv_temp(celsius)
		3:
			Escribir 'Hola!, Este ejercicio calcula la suma entre dos numeros';
			Escribir "Por avor ingresa un valor para el numero 1: ";
			Leer num1;
			Escribir "Por favor ingresa un valor para el numero 2: ";
			Leer num2;
			Escribir "La suma de los dos numeros es: ", num1+num2;
		De Otro Modo:
			Escribir "Por favor escribe un numero adecuado"
			Escribir probarEjercicios(x);
		4:
			Escribir 'Hola!, Este ejercicio calcula el promedio de tres calificaciones';
			Escribir "Por avor ingresa un valor para la nota 1: ";
			Leer nota1;
			Escribir "Por favor ingresa un valor para el nota 2: ";
			Leer nota2;
			Escribir "Por favor ingresa un valor para el nota 3: ";
			Leer nota3;
			Escribir "El promedio de las notas es: ", (nota1+nota2+nota3)/3;
		5: 
			Escribir 'Hola!, Este ejercici determina si una persona es mayor de edad';
			Escribir "Por avor ingresa tu edad: ";
			Leer edad
			Si edad >= 18 Entonces
				Escribir "Eres mayor de edad"
			SiNo
				Escribir "Eres menor de edad"
			Fin Si
	Fin Segun
FinFunción

Algoritmo admin_ejercicios
	
	Mientras respuesta <> "no" Hacer
		Escribir probarEjercicios(x);
		Escribir "Quieres volver a ver/realizar los ejercicios? [Si/No]"
		Leer respuesta
		respuesta <- Minusculas(respuesta)
	Fin Mientras

FinAlgoritmo


