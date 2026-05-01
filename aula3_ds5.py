temp = int(input('Digite a temperatura em C°:'))
umi = int(input('Digite a umidade em %:'))
if temp < 15:
   print('A temperatura é menor que 15 então está frio!')
   if umi <= 70:
       print('A umidade é menor que 70 então está frio e seco!')
   elif umi < 70:
       print('A umidade é maior que 70 então está frio e úmido!')
elif 15 <= temp < 30:
   print('A temperatura é maior que 15 e menor que 30 então está agradável!')
    if umi <= 70:
       print('A umidade é menor que 70 então está agradável e seco!')
   elif umi < 70:
       print('A umidade é maior que 70 então está agradável e úmido!')
elif 30 <= temp:
   print('A temperatura é maior que 30 então está quente!')
   if umi <= 70:
       print('A umidade é menor que 70 então está seco!')
   elif umi < 70:
       print('A umidade é maior que 70 então está abafado!')