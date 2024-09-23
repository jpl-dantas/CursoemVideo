nums = []
r = ''
while True:
    nu = int(input('Digite um número: '))
    if nu not in nums:
        nums.append(nu)
    else:
        print('Valor já adicionado anteriormente, tente outro número.')
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
print(f'Você digitou os valores: {sorted(nums)}')
