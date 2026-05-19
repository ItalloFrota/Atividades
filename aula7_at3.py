def primos (n):
    if n <= 1:
        return 'Não é primo'
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 'É primo'
    if n % 2 == 0:
        return 'Não é primo'
    elif n % 3 == 0:
        return 'Não é primo'
    elif n % 5 == 0:
        return 'Não é primo'
    elif n % 7 == 0:
        return 'Não é primo'
    else:
        return 'É primo'   
n = int(input("Digite um número: "))
resultado = primos(n)
print(resultado)