num = int(input('Digite um número inteiro: '))
print('\033[31m-\033[m' * 40)
print('1 - Número Binário')
print('2 - Número Octal')
print('3 - Número Exadecimal')
print('\033[31m-\033[m' * 40)
opc = int(input(f'Qual das opções acima você deseja converter o número {num}? '))
if opc == 1:
    print(f'O número {num} em binário é \033[32m{bin(num)}\033[m.')
elif opc == 2:
    print(f'O número {num} em octal é \033[32m{oct(num)}\033[m.')
elif opc == 3:
    print(f'O número {num} em hexadecimal é \033[32m{hex(num)}\033[m.')
else:
    print('Você não digitou um número de 1 a 3.')
