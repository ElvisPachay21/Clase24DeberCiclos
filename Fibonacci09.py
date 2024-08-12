def fibonacci(n):
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

n_term = int(input("¿Cuántos términos de la serie de Fibonacci deseas ver? "))

serie_fibonacci = fibonacci(n_term)

print(f"Los primeros {n_term} términos de la serie de Fibonacci son: {serie_fibonacci}")
