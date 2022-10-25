val = float(input('Digire o valor do produto: R$'))

des = val - (val * 5 / 100) 

print('O produto com desconto é de R${:.2f}'.format(des))