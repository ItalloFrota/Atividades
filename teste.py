def pares_impares(lista):
    par = []
    impar = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return par, impar
while True:
    caixa = []
    while True:
        numeros = input('DIGITE UM número para saber se é par ou impar(se quiser para degite F)')
        if numeros.isalpha():
            if numeros == 'F':
                break
            else:
                print('por favor digite um número ou f')
        numeros_inteiros = int(numeros)
        caixa.append(numeros_inteiros)
    if caixa == []:
        print('Erro, digite um número ou mais!')
    else:
        par, impar = pares_impares(caixa)
        print(f'os pares são: {par}\nos impares são: {impar}')