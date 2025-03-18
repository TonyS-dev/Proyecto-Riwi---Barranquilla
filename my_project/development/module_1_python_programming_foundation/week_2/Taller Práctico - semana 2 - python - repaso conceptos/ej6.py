# Escribe un programa que recorra una cadena de texto utilizando un ciclo for. Durante la iteración, 
# si el carácter es una vocal (mayúscula o minúscula), debe imprimir "Vocal" y continuar con el 
# siguiente carácter. Si el carácter es un espacio en blanco, el ciclo debe detenerse con la 
# instrucción. Al final, el programa debe mostrar la cantidad total de vocales encontradas en la 
# cadena de texto. 
 
sentence = input("Por favor ingresa una frase: ")
vowels = []
vowels_quantity = 0
for character in sentence:
    if character in "aeiouAEIOU":
        vowels.append(character)
        vowels_quantity += 1
        print(f"{character} es una Vocal")
    elif character in " ":
        print("Espacio en blanco encontrado, deteniendo programa...")
        break

print(f"\nHubo {vowels_quantity} vocales, las cuales fueron: \n{vowels}")