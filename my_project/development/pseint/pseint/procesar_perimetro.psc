Funci�n perimetro <- calc_perimetro (lado)
	perimetro <- lado*4;
FinFunci�n

Algoritmo procesar_perimetro
	Definir lado Como Entero;
	Escribir 'Hola!, Este programa calcula el per�metro de un cuadrado';
	Definir confirmacion Como L�gico;
	Mientras confirmacion==Falso Hacer
		Escribir 'Por favor ingresa la medida del lado del cuadrado:';
		Leer lado;
		Escribir 'El lado es: ', lado;
		Escribir 'Es esto Verdadero o Falso?';
		Leer confirmacion;
	FinMientras
	Escribir 'El per�metro es: ', calc_perimetro(lado);
FinAlgoritmo

