Función fahrenheit <- conv_temp (celsius)
fahrenheit <- (celsius*9/5)+32;
FinFunción

Algoritmo conv_temperatura
	Definir celsius Como Entero;
	Escribir 'Hola!, Este programa convierte la temperatura de grados Celsius a Fahrenheit';
	Definir confirmacion Como Lógico;
	Mientras confirmacion==Falso Hacer
		Escribir 'Por favor ingresa la temperatura en grados Celsius:';
		Leer celsius;
		Escribir 'La temperatura es: ', celsius,'° Celsius';
		Escribir 'Es esto Verdadero o Falso?';
		Leer confirmacion;
	FinMientras
	Escribir 'La temperatura en grados Fahrenheit es: ', conv_temp(celsius);
FinAlgoritmo

