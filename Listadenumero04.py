numeros = [75, 5, 98, 36, 25, 14, 45]

minimo = numeros[0] 

for numero in numeros:
    if numero < minimo:
        minimo = numero

print("El número menor en la lista es:", minimo)
