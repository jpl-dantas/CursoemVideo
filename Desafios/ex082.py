nums = []
numi = []
nump = []
r = ''
while True:
    nu = int(input('Digite um número inteiro: '))
    nums.append(nu)
    if nu % 2 == 0:
        nump.append(nu)
    else:
        numi.append(nu)
    while r != 'S' and r != 'N':
        r = input('Você quer continuar? [S/N]: ').upper()
        if r == 'S':
            print('-' * 43)
        elif r == 'N':
            print('-' * 43)
            break
        else:
            print('Por favor digite uma resposta válida')
    if r == 'N':
        break
    r = ''

if len(nums) > 1:
    print(f'Você digitou os valores: {nums}')
else:
    print(f'Você digitou apenas o valor: {nums}')
if len(nump) >= 1:
    if len(nump) > 1:
        print(f'Desses valores, estes foram os valores pares: {nump}')
    else:
        print(f'Só existe um número par: {nump}')
else:
    if len(nums) > 1:
        print('Desses valores, não teve nenhum valor par.')
    else:
        print('Esse valor não é par.')
if len(numi) >= 1:
    if len(numi) > 1:
        print(f'E esses foram os valores ímpares: {numi}')
    else:
        print(f'Só existe um número ímpar: {numi}')
else:
    if len(nums) > 1:
        print('Desses valores, não teve nenhum valor ímpar.')
    else:
        print('Esse valor não é ímpar.')
