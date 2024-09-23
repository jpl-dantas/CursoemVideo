from datetime import date
ann = int(input('Garoto, em que ano você nasceu? '))
idd = date.today().year - ann
print(f'Você tem {idd} anos.')
if idd == 17 or idd == 18:
    print('Está na hora de se alistar no exército militar.')
elif idd < 17 or idd < 18:
    print('Por enquanto, você não precisa se alistar no exército militar.'
          f'\nAinda falta(m) {17 - idd} ano(s) para você poder se alistar.')
elif idd > 17 or idd > 18:
    print('Você já ultrapassou a idade de alistamento obrigatório.')
    r = input('Você foi aprovado? ').upper()
    if r == 'SIM' or r == 'CLARO':
        print('Muito bem!')
    elif r == 'NÃO' or r == 'NAO':
        print('Sem problema.')
