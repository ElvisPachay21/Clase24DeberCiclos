altura = int(input("Introduce la altura de la pirámide: "))

for i in range(altura):
    print(' ' * (altura - i - 1), end='')
    print('*' * (2 * i + 1))
