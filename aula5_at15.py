while True:
    num1 = float(input('Digite o primeiro número:'))
    operacao = input('+;\n-;\n/;\nx;\nDigite a operação:') 
    num2 = float(input('Digite o segundo número:'))
    match operacao:
        case '+':
            print(f'A soma de {num1} + {num2} = {num1 + num2}')
        case '-':
            print(f'A subitração de {num1} - {num2} = {num1 - num2}')
        case '/':
            print(f'A divisão de {num1} / {num2} = {num1 / num2}')
        case 'x':
            print(f'A mutiplicação de {num1} x {num2} = {num1 * num2}')
        case _:
            print('Operação invalida!')
    fim = input('Se quiser parar digite "FIM" se quiser continuar aperte "ENTER"').upper()
    if fim == 'FIM':
        print("Calculadora ecerada")
        break