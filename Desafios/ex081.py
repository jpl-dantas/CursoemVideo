nums = []
r = ''
while True:
    nums.append(int(input('Digite um número: ')))
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
    s = 's'
else:
    s = ''
print(f'Você digitou {len(nums)} número{s}.')
nums.sort(reverse=True)
print(f'Os valores digitados foram: {nums}')
if 5 in nums:
    print(f'O valor 5 aparece na lista na posição {nums.index(5)}')
else:
    print('O valor 5 não aparece na lista.')
