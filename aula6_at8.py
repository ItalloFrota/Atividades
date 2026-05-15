def sequencia_númerica(num):
    for i in range(1, num + 1):
        print(str(i) * i)
numero = int(input("Digite um número inteiro para ver um piramide de números: "))
print('=' * 30)
print(f"Piramide de números até {numero}:")
print('=' * 30)
print('Sequência numérica:')
print('=' * 30)
sequencia_númerica(numero)   