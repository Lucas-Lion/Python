km = float(input('Digite a quantidade de Km rodados:'))
day = float(input('Digite a quantidade de dias alugados:'))

cal = (day * 60) + (km * 0.15)

print('O preço a pagar é de R${:.2f}'.format(cal))