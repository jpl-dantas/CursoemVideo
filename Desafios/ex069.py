TiP = ' FAST CADASTRO '
print('=' * 43)
print(f'{TiP:-^43}')
print('=' * 43)
r = ''
pm = sm = m20 = 0
np = 1
while True:
    i = int(input(f'Qual é a idade da {np}ª pessoa? '))
    if i <= 0 or i >= 201:
        print('-> Por favor, digite uma idade válida.')
    elif i >= 1 and i <= 200:
        if i >= 18:
            pm += 1
        break

while True:
    s = input(f'Qual é o sexo da {np}ª pessoa? [M/F]: ').upper()
    if s == 'M' or s == 'F':
        np += 1
        if i < 20 and s == 'F':
            m20 += 1
        if s == 'M':
            sm += 1
        break
    else:
        print('Por favor, digite uma opção correta (M ou F).')
print('=' * 43)
while True:
    r = input('Você quer cadastrar mais pessoas? [S/N]: ').upper()
    if r == 'N':
        print('=' * 43)
        break
    elif r == 'S':
        print('=' * 43)
        while True:
            i = int(input(f'Qual é a idade da {np}ª pessoa? '))
            if i <= 0 or i >= 201:
                print('-> Por favor, digite uma idade válida.')
            elif i >= 1 and i <= 200:
                if i >= 18:
                    pm += 1
                break

        while True:
            s = input(f'Qual é o sexo da {np}ª pessoa? [M/F]: ').upper()
            if s == 'M' or s == 'F':
                np += 1
                if i < 20 and s == 'F':
                    m20 += 1
                if s == 'M':
                    sm += 1
                break
            else:
                print('Por favor, digite uma opção correta (M ou F).')
    else:
        print('Por favor, escolha uma opção correta (S ou N).')
    print('=' * 43)
print(f'Total de pessoas maiores de 18 anos: {pm} ')
print(f'Total de pessoas do sexo masculino: {sm}')
print(f'Total de mulheres com menos de 20 anos: {m20}')
print('=' * 43)
TiPC = ' OBRIGADO POR USAR A FAST CADASTRO '
TiPC1 = ' TENHA UM ÓTIMO DIA '
print(f'{TiPC:-^43}')
print(f'{TiPC1:-^43}')
print('=' * 43)
