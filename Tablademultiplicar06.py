numero = int(input("Introduce el número para generar su tabla de multiplicar: "))


print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
