Algoritmo calculo_factorial
	Definir input, numActual, total Como Entero
	
	Escribir "~~~Este es el ejercicio 4~~~"
	Escribir "El cual calcula el factorial de un numero"
	
	Escribir "Ingresa un número para calcular su factorial:"
	Leer input
	total = input
	
	Escribir input, "!", " Es igual a: "
	
	Para numContador <- 1 Hasta input - 1 Con Paso 1 Hacer
		
		numActual = input - numContador
		
		Escribir "Paso ", numContador, ": ", total, " x ", numActual, " = ", total * numActual
		
		total = total * numActual
		
	Fin Para
	
	Escribir "El total es: ", total
	Escribir "----------------Ejercicio finalizado----------------"
FinAlgoritmo

