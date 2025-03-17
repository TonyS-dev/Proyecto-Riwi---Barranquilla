Algoritmo sumatoria_de_los_primeros_10_números_naturales
    
	Definir totalCiclo, numContador Como Entero
    
	Escribir "~~~Este es el ejercicio 2~~~"
	Escribir "El cual hace  la sumatoria de los primeros 10 números naturales"
	
	Escribir "/// Bucle para ///"
	totalCiclo <- 0 
    Para numContador <- 1 Hasta 10 Con Paso 1 Hacer
        totalCiclo <- totalCiclo + numContador
        Escribir "Paso ", numContador, ": ", totalCiclo - numContador, " + ", numContador, " = ", totalCiclo
    FinPara
	Escribir "El total fue: ", totalCiclo
	
	Escribir "/// Bucle mientras ///"
	totalCiclo <- 0 
	Mientras numContador < 10 Hacer
	   numContador = numContador + 1
	   totalCiclo <- totalCiclo + numContador
        Escribir "Paso ", numContador, ": ", totalCiclo - numContador, " + ", numContador, " = ", totalCiclo
   Fin Mientras
   Escribir "El total fue: ", totalCiclo
   Escribir "----------------Ejercicio finalizado----------------"
FinAlgoritmo
