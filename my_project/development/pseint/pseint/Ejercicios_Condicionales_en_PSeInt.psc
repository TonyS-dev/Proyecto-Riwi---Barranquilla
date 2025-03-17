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
	Definir contraseña Como Caracter
	contraseña = "admin123"
	Definir verificarContraseña como Caracter
	Definir num1, num2, num3, highest Como Real
	Definir confirmacion Como Caracter
	Escribir "<<<Este programa muestra los ejercicios de condicionales de Riwi en Pseint>>>"
	Repetir
		Escribir "/// Porfavor ingresa un numero para acceder a un ejercicio [1, 2. 3, 4, 5] ///"
		Repetir
			Leer numEjercicio
			Segun numEjercicio Hacer
				1:
					Escribir numeroDeEjercicio(numEjercicio), "El cual determina si un número es positivo, negativo o cero"
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
						Escribir "Eres un niño"
					SiNo
						Si edad < 18 Entonces
							Escribir "Eres un adolescente"
						SiNo
							Escribir "Eres un adulto"
						Fin Si
					Fin Si
					Escribir ejercicioFinalizado(x)
				3:	
					Escribir numeroDeEjercicio(numEjercicio),"El cual brinda un menú de opciones con según"
					Escribir "/// Porfavor ingresa un numero para acceder a una operación [1, 2. 3, 4] ///"
					Escribir "1: Sumar"
					Escribir "2: Restar"
					Escribir "3: Multiplicar"
					Escribir "4: Dividir"
					Repetir
						Leer option
						Segun option Hacer
							1:
								Escribir "Esta es la operación 1 la cual suma, "
								Escribir "Porfavor ingresa el primer numero a sumar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a sumar"
								Leer num2
								Escribir "El resultado es: ", (num1 + num2)
							2:
								Escribir "Esta es la operación 2 la cual resta, "
								Escribir "Porfavor ingresa el primer numero a restar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a restar"
								Leer num2
								Escribir "El resultado es: ", (num1 - num2)
							3:
								Escribir "Esta es la operación 3 la cual multiplica, "
								Escribir "Porfavor ingresa el primer numero a multiplicar"
								Leer num1
								Escribir "Porfavor ingresa el segundo numero a multiplicar"
								Leer num2
								Escribir "El resultado es: ", (num1 * num2)
							4:
								Escribir "Esta es la operación 4 la cual divide, "
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
					Escribir numeroDeEjercicio(numEjercicio), "El cual valida la contraseña"
					Escribir "/// Por favor digite la contraseña ///"
					Leer verificarContraseña
					Si verificarContraseña == contraseña Entonces
						Escribir "Acceso permitido"
					SiNo
						Escribir "Acceso denegado"
					Fin Si
					Escribir ejercicioFinalizado(x)
				5:
					Escribir numeroDeEjercicio(numEjercicio), "El cual determina el mayor de tres números"
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







