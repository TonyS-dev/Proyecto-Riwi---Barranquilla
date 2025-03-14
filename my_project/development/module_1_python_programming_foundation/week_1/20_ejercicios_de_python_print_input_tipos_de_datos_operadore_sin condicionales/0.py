# Script para administrar los 20 ejercicios de print sin condicional
import importlib

def switch(seleccion):
    match seleccion:
        case 1:
            return "1"
        case 2:
            return "2"
        case 3:
            return "3"
        case 4:
            return "4"
        case 5:
            return "5"
        case 6:
            return "6"
        case 7:
            return "7"
        case 8:
            return "8"
        case 9:
            return "9"
        case 10:
            return "10"
        case 11:
            return "11"
        case 12:
            return "12"
        case 13:
            return "13"
        case 14:
            return "14"
        case 15:
            return "15"
        case 16:
            return "16"
        case 17:
            return "17"
        case 18:
            return "18"
        case 19:
            return "19"
        case 20:
            return "20"
        case _:
            raise ValueError("El número ingresado no está dentro del rango permitido.")

seleccion = int(input("Ingrese un numero de 1 a 20 para seleccionar un ejercicio: "))
resultado = switch(seleccion)

for i in range(1, 21):

    importlib.import_module(resultado)