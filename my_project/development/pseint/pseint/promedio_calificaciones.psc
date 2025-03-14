Algoritmo promedio_calificaciones
	
	Definir calificacion, suma, promedio Como Real
	Definir numeroContador Como Entero
	
	Escribir "~~~Este es el ejercicio 5~~~"
	Escribir "El cual calcula el promedio de 5 calificaciones"
	
	suma = 0
	
	Escribir "/// Ingreso de calificaciones ///"
	Para numeroContador <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingrese la calificación ", numeroContador, ":"
		Leer calificacion
		suma <- suma + calificacion
	Fin Para
	
	promedio = suma / 5
	
	Escribir "/// Resultado ///"
	Escribir "El promedio es: ", promedio
	
	Si promedio >= 6 Entonces
		Escribir "El estudiante ha aprobado"
	Sino
		Escribir "El estudiante ha reprobado"
	Fin Si
	
	Escribir "----------------Ejercicio finalizado----------------"
FinAlgoritmo