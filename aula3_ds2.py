salario = float(input('Qual o salário:'))
tempo = int(input('Quantos anos de empresa:'))
nd = int(input('Quantos dependentes:'))
if tempo >= 10:
    sf = salario + (20 / 100 * salario)
    print('Bônus por tempo 20%:', (20 / 100 * salario))
elif 5 <= tempo < 10:
    sf = salario + (10 / 100 * salario)
    print('Bônus por tempo 10%:', 10 / 100 * salario)
elif 5 > tempo :
    sf = salario + (5 / 100 * salario)
    print('Bônus por tempo 5%:', 5 / 100 * salario)
sf += 100 * nd
print('Bônus por dependente:', 100 * nd)
print('O salário final é:', sf)