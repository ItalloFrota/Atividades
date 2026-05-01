total = 0
quantidade_total = 0
itens = []
while True:
    nome = input('digite o nome do pruduto, caso queira finalizar digite (fim):').title()
    if nome == 'Fim':
        break
    preço = float(input('Digite o preço:'))
    quantidade = float(input('Digite a quantidade:'))
    subtotal = preço * quantidade
    print(f'Nome  do produto: {nome}\nSubtotal: {subtotal}')
    itens.append(nome)
    quantidade_total += quantidade
    total += subtotal
print(f'itens: {itens}\nQantidade: {quantidade_total}\ntotal: {total}')