Funcion x <- ejercicioFinalizado (x)
	Escribir "----------------Ejercicio finalizado----------------"
Fin Funcion

Funcion x <- numeroDeEjercicio (numEjercicio)
	Escribir "~~~Este es el ejercicio ", numEjercicio,"~~~"
Fin Funcion

Algoritmo Ejercicios_de_bucles_en_PSeInt
	
	// Variables Definidas //
	Definir totalCiclo, numeroContador, input, numeroActual, total Como Entero
	Definir calificacion, suma, promedio Como Real
	
	// Ejecución del codigo //
	Escribir "<<<Este programa muestra los ejercicios de bucles de Riwi en Pseint>>>"
	Repetir
		Escribir "/// Porfavor ingresa un numero para acceder a un ejercicio [1, 2. 3, 4, 5] ///"
		Repetir
			Leer numEjercicio
			Segun numEjercicio Hacer
				1:
					Escribir numeroDeEjercicio(numEjercicio), "El cual cuenta del 1 al 10 con diferentes bucles"
					
					Escribir "/// Bucle mientras ///"
					numeroContador = 1
					Mientras numeroContador <= 10 Hacer
						Escribir numeroContador
						numeroContador <- numeroContador +1
					Fin Mientras
					
					Escribir "/// Bucle repetir hasta que ///"
					numeroContador = 1
					Repetir
						Escribir numeroContador
						numeroContador = numeroContador +1
					Hasta Que numeroContador > 10
					
					Escribir "/// Bucle para ///"
					Para numeroContador <- 1 Hasta 10 Con Paso 1 Hacer
						Escribir numeroContador
					Fin Para
					
					Escribir ejercicioFinalizado(x)
				2:
					Escribir numeroDeEjercicio(numEjercicio), "El cual hace  la sumatoria de los primeros 10 números naturales"
					
					Escribir "/// Bucle para ///"
					totalCiclo <- 0 
					Para numeroContador <- 1 Hasta 10 Con Paso 1 Hacer
						totalCiclo <- totalCiclo + numeroContador
						Escribir "Paso ", numeroContador, ": ", totalCiclo - numeroContador, " + ", numeroContador, " = ", totalCiclo
					FinPara
					Escribir "El total fue: ", totalCiclo
					
					Escribir "/// Bucle mientras ///"
					totalCiclo <- 0 
					Mientras numeroContador < 10 Hacer
						numeroContador = numeroContador + 1
						totalCiclo <- totalCiclo + numeroContador
						Escribir "Paso ", numeroContador, ": ", totalCiclo - numeroContador, " + ", numeroContador, " = ", totalCiclo
					Fin Mientras
					
					Escribir "El total fue: ", totalCiclo
					Escribir ejercicioFinalizado(x)
				3:	
					Escribir numeroDeEjercicio(numEjercicio),"El cual cuenta regresivamente de 10 a 1"
					numeroContador = 10
					Escribir "Tripulación preparense para el despegue"
					Escribir "Cuenta regresiva en:"
					Mientras numeroContador > 0 Hacer
						Escribir numeroContador
						numeroContador = numeroContador - 1
					Fin Mientras
					Escribir "¡Despegue!"
					Escribir ejercicioFinalizado(x)
				4:	
					Escribir numeroDeEjercicio(numEjercicio), "El cual calcula el factorial de un numero"
					Escribir "Ingresa un número para calcular su factorial:"
					Leer input
					total = input
					
					Escribir input, "!", " Es igual a: "
					
					Para numeroContador <- 1 Hasta input - 1 Con Paso 1 Hacer
						
						numeroActual = input - numeroContador
						
						Escribir "Paso ", numeroContador, ": ", total, " x ", numeroActual, " = ", total * numeroActual
						
						total = total * numeroActual
						
					Fin Para
					
					Escribir "El total es: ", total
					Escribir ejercicioFinalizado(x)
				5:
					Escribir numeroDeEjercicio(numEjercicio), "El cual calcula el promedio de 5 calificaciones"
				    
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
					Escribir ejercicioFinalizado(x)
				De Otro Modo:
					Escribir "!!! Por favor escribe un numero valido !!!"
			Fin Segun
		Hasta Que numEjercicio == 1 o numEjercicio == 2 o numEjercicio == 3 o numEjercicio == 4 o numEjercicio == 5
		Escribir "/// Quieres seguir realizando ejercicios? ///"		
		Repetir
			Escribir "!!! Por favor escribe Si o No !!!"
			Leer confirmacion
		Hasta Que confirmacion == "Si" o confirmacion == "si" o confirmacion == "No" o confirmacion == "no"
	Hasta Que confirmacion == "No" o confirmacion == "no"
FinAlgoritmo







