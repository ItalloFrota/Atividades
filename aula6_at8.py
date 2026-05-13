def sequencia_númerica(num):
    for i in range(1, num + 1):
        print(str(i) * i)
numero = int(input("Digite um número inteiro: "))
sequencia_númerica(numero)