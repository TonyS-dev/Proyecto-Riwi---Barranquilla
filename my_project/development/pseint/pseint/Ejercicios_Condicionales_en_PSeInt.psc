Funcion x <- ejercicioFinalizado (x)
	Escribir "----------------Ejercicio finalizado----------------"
Fin Funcion

Funcion x <- numeroDeEjercicio (numEjercicio)
	Escribir "~~~Este es el ejercicio ", numEjercicio,"~~~"
Fin Funcion

Algoritmo Ejercicios_Condicionales_en_PSeInt
	Definir numEjercicio Como Entero
	Definir edad Como Entero
	Definir option como Entero
	Definir contrase�a Como Caracter
	contrase�a = "admin123"
	Definir verificarContrase�a como Caracter
	Definir num1, num2, num3, highest Como Real
	Definir confirmacion Como Caracter
	Escribir "<<<Este programa muestra los ejercicios de condicionales de Riwi en Pseint>>>"
	Repetir
		Escribir "/// Porfavor ingresa un numero para acceder a un ejercicio [1, 2. 3, 4, 5] ///"
		Repetir
			Leer numEjercicio
			Segun numEjercicio Hacer
				1:
					Escribir numeroDeEjercicio(numEjercicio), "El cual determina si un n�mero es positivo, negativo o cero"
					Escribir "/// Por favor ingresa un numero ///"
					Leer num1
					Si num1 == 0 Entonces
						Escribir "El numero ingresado es cero"
					SiNo
						Si num1 < 0 Entonces
							Escribir "El numero ingresado es negativo"
						SiNo
							Escribir "El numero ingresado es positivo"
						Fin Si
					Fin Si
					Escribir ejercicioFinalizado(x)
				2:
					Escribir numeroDeEjercicio(numEjercicio), "El cual clasifica edades"
					Escribir "/// Por favor ingresa tu edad ///"
					Leer edad
					Si edad < 12 Entonces
						Escribir "Eres un ni�o"
					SiNo
						Si edad < 18 Entonces
							Escribir "Eres un adolescente"
						SiNo
							Escribir "Eres un adulto"
						Fin Si
					Fin Si
					Escribir ejercicioFinalizado(x)
				3:	
					Escribir numeroDeEjercicio(numEjercicio),"El cual brinda un men� de opciones con seg�n"
					Escribir "/// Porfavor ingresa un numero para acceder a una operaci�n [1, 2. 3, 4] ///"
					Escribir "1: Sumar"
					Escribir "2: Restar"
					Escribir "3: Multiplicar"
					Escribir "4: Dividir"
					Repetir
						Leer option
						Segun option Hacer
							1:
								Escribir "Esta es la operaci�n 1 la cual suma, "
								Escribir "Porfavor ingresa el primer numero a sumar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a sumar"
								Leer num2
								Escribir "El resultado es: ", (num1 + num2)
							2:
								Escribir "Esta es la operaci�n 2 la cual resta, "
								Escribir "Porfavor ingresa el primer numero a restar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a restar"
								Leer num2
								Escribir "El resultado es: ", (num1 - num2)
							3:
								Escribir "Esta es la operaci�n 3 la cual multiplica, "
								Escribir "Porfavor ingresa el primer numero a multiplicar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a multiplicar"
								Leer num2
								Escribir "El resultado es: ", (num1 * num2)
							4:
								Escribir "Esta es la operaci�n 4 la cual divide, "
								Escribir "Porfavor ingresa el primer numero a dividir"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a dividir"
								Leer num2
								Escribir "El resultado es: ", (num1 / num2)
							De Otro Modo:
								Escribir "!!! Por favor escribe un numero valido !!!"
						Fin Segun
					Hasta Que option == 1 o option == 2 o option == 3 o option == 4
					Escribir ejercicioFinalizado(x)
				4:	
					Escribir numeroDeEjercicio(numEjercicio), "El cual valida la contrase�a"
					Escribir "/// Por favor digite la contrase�a ///"
					Leer verificarContrase�a
					Si verificarContrase�a == contrase�a Entonces
						Escribir "Acceso permitido"
					SiNo
						Escribir "Acceso denegado"
					Fin Si
					Escribir ejercicioFinalizado(x)
				5:
					Escribir numeroDeEjercicio(numEjercicio), "El cual determina el mayor de tres n�meros"
					Escribir "/// Por favor ingresa 3 numeros ///"
					Leer num1, num2, num3
					Si num1 > num2 y num1 > num3 Entonces
						highest = num1
					SiNo
						Si num2 > num3 Entonces
							highest = num2
						SiNo
							highest = num3
						Fin Si
					Fin Si
					Escribir "El numero mayor es: ", highest
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







