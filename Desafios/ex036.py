vac = float(input('Digite o preço da casa: R$'))
vas = float(input('Digite o quanto você recebe: R$'))
qaa = int(input('Durante quantos anos você deseja financiar essa casa? '))
vpm = (vac / qaa) / 12
tvas = (vas / 100) * 30
# print(vpm)
# print(tvas)
if vpm >= tvas:
    print(f'Infelizmente nós \033[31mnão iremos liberar\033[m o empréstimo para financiar esta casa.'
          f'\nO valor da prestação mensal seria de R${vpm:.2f}, o que excede 30% do seu salário.')
else:
    print('O empréstimo foi \033[32maprovado!')
