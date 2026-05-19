def fibonacci(n):
    sequencia = []
    for i in range(n):
        if i == 0:
            sequencia.append(0)
        elif i == 1:
            sequencia.append(1)
        else:
            sequencia.append(sequencia[i - 1] + sequencia[i - 2])
    return sequencia
n = int(input("Digite o número de termos da sequência de Fibonacci: "))
resultado = fibonacci(n)
print("Sequência de Fibonacci:")
print(resultado)