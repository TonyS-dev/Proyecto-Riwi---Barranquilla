Función perimetro <- calc_perimetro (lado)
	perimetro <- lado*4;
FinFunción

Algoritmo procesar_perimetro
	Definir lado Como Entero;
	Escribir 'Hola!, Este programa calcula el perímetro de un cuadrado';
	Definir confirmacion Como Lógico;
	Mientras confirmacion==Falso Hacer
		Escribir 'Por favor ingresa la medida del lado del cuadrado:';
		Leer lado;
		Escribir 'El lado es: ', lado;
		Escribir 'Es esto Verdadero o Falso?';
		Leer confirmacion;
	FinMientras
	Escribir 'El perímetro es: ', calc_perimetro(lado);
FinAlgoritmo

