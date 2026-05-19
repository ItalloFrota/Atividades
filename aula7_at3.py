def primos (n):
    if n <= 1:
        return 'Não é primo'
    elif n == 2:
        return 'É primo'
    for i in range(2, n):
        if n % i == 0:
            return 'Não é primo'
    return 'É primo'

n = int(input("Digite um número: "))
resultado = primos(n)
print(resultado)