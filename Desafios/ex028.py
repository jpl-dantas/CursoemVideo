import random
num = int(input('Qual vai ser o próximo número de 0 a 5? '))
numa = random.randint(0, 5)
if num == numa:
    print('Você acertou o número!')
    ez = input('Você achou fácil?: ').upper()
    if ez == 'NÃO':
        print('Então o próximo será mais dificil ainda.')
    if ez == 'SIM':
        print('Então acerte o próximo número:')
    numad = random.randint(0, 50)
    numd = int(input('Qual vai ser o próximo número de 0 a 50? '))
    if numd == numad:
        print('Rapaz, tu ta de hack.')
    else:
        print(f'Você errou, o número era {numad}. Cadê o bonzão agora? KKKKKKKK')
else:
    print(f'O número era {numa}. Tente novamente!')
