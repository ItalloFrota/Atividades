print('======= SEQUENCIA DE FIBONACCI =======\n')
num = int(input("Dgite um número inteiro:"))
a, b = 0, 1
for i in range(num):
    print(a)
    a, b = b, a + b
c, d = 0, 1
fibo = []
for i in range(num):
    fibo.append(c)
    c, d = d, c + d
print(fibo)