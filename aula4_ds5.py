nome = input("Digite seu nome:")
nomepr = input("Digite o nome do produto nome:")
categoria = input("Digite a categoria do produto (eletrônico, alimento, vestuário):")
preço = float(input("Digite o preço do produto:"))
qnt = float(input("Digite a quantidade:"))
forma = input("Digite a forma de pagamento (pix, cartão):")
print('======================================================================================\n')
subtotal = preço * qnt
print(nome.title(), '\n')
print(nomepr.upper(), '\n')
print('======================================================================================\n')
print('Preço por quantidade:', subtotal)
match categoria:
    case 'eletrônico':
        subtotal -= 5 / 100 * subtotal
        print('Desconto por eletrônicos de 5%:', subtotal)
    case 'alimento':
        subtotal -= 10 / 100 * subtotal
        print('Desconto por alimetos de 10%:', subtotal)
    case 'vestuário':
        subtotal -= 15 / 100 * subtotal
        print('Desconto por alimetos de 15%:', subtotal)
match forma:
    case 'pix':
        subtotal -= 5 / 100 * subtotal
        print(f'5% de desconto em pix:{subtotal:.2f}')
    case 'cartão':
        print('Não há desconto em pagamentos com cartão:', subtotal)
        
if subtotal >= 200:
    print('frete grátis (COMPRA ACIMA DE R$ 200)\n')
else:
    print('frete de 20 (COMPRA ABAIXO DE R$ 200)\n')
    subtotal += 20
print('======================================================================================\n')
print(f'VALOR FINAL:,{subtotal:.2f}')