Algoritmo Ejercicios_Condicionales_en_PSeInt
	Definir numEjercicio Como Entero
	Escribir "Este programa muestra los ejercicios de condicionales de Riwi en Pseint"
	Escribir "Porfavor ingresa un numero para acceder a un ejercicio [1, 2. 3, 4, 5]"
	Leer numEjercicio
	Segun numEjercicio Hacer
		1:
			Definir numEjercicio1 Como Entero
			Escribir "Este es el ejercicio 1, el cual determina si un n�mero es positivo, negativo o cero"
			Escribir "Por favor ingresa un numero"
			Leer numEjercicio1
			Si numEjercicio1 == 0 Entonces
				Escribir "El numero ingresado es cero"
			SiNo
				Si numEjercicio1 < 0 Entonces
					Escribir "El numero ingresado es negativo"
				SiNo
					Escribir "El numero ingresado es positivo"
				Fin Si
			Fin Si
			Escribir "Ejercicio finalizado"
		2:
			Definir edad Como Entero
			Escribir "Este es el ejercicio 2, el cual clasifica edades"
			Escribir "Por favor ingresa tu edad"
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
		3:	
			Definir option como Entero
			Definir num1 Como Real
			Definir num2 Como Real
			Escribir "Este es el ejercicio 3, el cual brinda un men� de opciones con seg�n"
			Escribir "Porfavor ingresa un numero para acceder a una operaci�n [1, 2. 3, 4]"
			Escribir "1: Sumar"
			Escribir "2: Restar"
			Escribir "3: Multiplicar"
			Escribir "4: Dividir"
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
						Escribir "Por favor escribe un numero valido"
				Fin Segun
		4:	
			Definir contrase�a Como Caracter
			contrase�a = "admin123"
			Escribir "Este es el ejercicio 4, el cual valida la contrase�a"
			Escribir "Por favor digite la contrase�a"
			Leer verificarContrase�a
			Si verificarContrase�a == contrase�a Entonces
				Escribir "Acceso permitido"
			SiNo
				Escribir "Acceso denegado"
			Fin Si
		5:
			Definir nume1, nume2, nume3, highest Como Real
			Escribir "Este es el ejercicio 5, el cual determina el mayor de tres n�meros"
			Escribir "Por favor ingresa 3 numeros"
			Leer nume1, nume2, nume3
			Si nume1 > nume2 y nume1 > nume3 Entonces
				highest = nume1
			SiNo
				Si nume2 > nume3 Entonces
					highest = nume2
				SiNo
					highest = nume3
				Fin Si
			Fin Si
			Escribir "El numero mayor es: ", highest
		De Otro Modo:
			Escribir "Por favor escribe un numero valido"
	Fin Segun
FinAlgoritmo
