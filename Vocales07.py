texto = input("Introduce un texto para contar las vocales: ")

vocales = "aeiouáéíóú"


contador_vocales = 0

for caracter in texto.lower():  
    if caracter in vocales:
        contador_vocales += 1

print(f"El número total de vocales en el texto es: {contador_vocales}")
