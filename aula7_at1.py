def fatorial(n):
    fatorial_resultado = 1
    for i in range(1, n + 1):
        fatorial_resultado *= i
    return fatorial_resultado
num = int(input('digite um número inteiro para ver seu fatorial:'))
print(f'O fatorial de {num} = {fatorial(num)}')