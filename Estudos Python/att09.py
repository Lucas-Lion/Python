b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

a = b * h
tin = a / 2

print('A sua área é de {:.2f} e será necessário {:.0f}l de tinta para pintar a sua área.'.format(a, tin))