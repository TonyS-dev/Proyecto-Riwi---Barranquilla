Algoritmo contar_numeros_del_1_al_10_con_bucles
	
	Definir numCount Como Entero
	
	Escribir "~~~Este es el ejercicio 1~~~"
	Escribir "El cual cuenta del 1 al 10 con diferentes bucles"
	
	Escribir "/// Bucle mientras ///"
	numCount = 1
	Mientras numCount <= 10 Hacer
		Escribir numCount
		numCount <- numCount +1
	Fin Mientras
	
	Escribir "/// Bucle repetir hasta que ///"
	numCount = 1
	Repetir
		Escribir numCount
		numCount = numCount +1
	Hasta Que numCount > 10
	
	Escribir "/// Bucle para ///"
	Para numCount <- 1 Hasta 10 Con Paso 1 Hacer
		Escribir numCount
	Fin Para
	Escribir "----------------Ejercicio finalizado----------------"
FinAlgoritmo
