sal = float(input('Qual o seu salário? R$'))

rea = sal + (sal * 15 / 100)

print('Parabéns! Você ganhou um aumento, seu novo salário é de R${:.2f}'.format(rea))