vp = float(input('Digite o valor do produto: R$'))
print('-' * 5, '\033[4;32mFORMAS DE PAGAMENTO\033[m', '-' * 5)
print('1 - Dinheiro á vista -> \033[33m10% de desconto\033[m')
print('2 - Cartão á vista -> \033[33m5% de desconto\033[m')
print('3 - Cartão parcelado em até 2x')
print('4 - Cartão parecelado em 3x ou mais -> \033[31m20% de juros\033[m')
op1 = vp - (vp / 100) * 10
op2 = vp - (vp / 100) * 5
op3 = vp / 2
fp = input('Como você deseja pagar pelo produto (escolha um número)? ').upper()
if fp == '1':
    print('Você escolheu dinheiro á vista como forma de pagamento, o que permite'
          'que você tenha 10% de desconto no produto.')
    print(f'O valor total a pagar é de R${op1:.2f}')
elif fp == '2':
    print('Você escolheu cartão á vista como forma de pagamento, o que permite'
          'que você tenha 5% de desconto.')
    print(f'O valor total a pagar é de R${op2:.2f}')
elif fp == '3':
    print('Você escolheu cartão parcelado em até 2x como forma de pagamento, '
          'o que não muda o valor original do produto, \nporém, irá pagar metade do valor inteiro por mês.')
    print(f'O valor a pagar das 2 parcelas é de R${op3:.2f}')
elif fp == '4':
    print('Você escolheu cartão parcelado em até 3x ou mais como forma de pagamento, o que adiciona '
          'mais 20% de juros no valor do produto.')
    qp = int(input('Em quantas parcelas você deseja pagar pelo produto? '))
    op4 = qp / vp + (vp / 100) * 20
    if qp <= 2:
        print('A opção 4 é apenas para quem deseja pagar parcelas em até 3x ou mais no cartão.'
              '\nPor favor, escolha a opção 2 ou 3.')
    elif 3 <= qp <= 12:
        print(f'O valor a pagar das {qp} parcelas é de R${op4:.2f}')
    elif qp > 12:
        print('Você só pode parcelar até no máximo 12x.')
else:
    print('Você não digitou uma opção de 1 a 4.')
