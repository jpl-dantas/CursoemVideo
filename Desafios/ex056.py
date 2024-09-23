femi = 0
masc = 0
hvelho = 0
nis1 = ''
nis2 = ''
nis3 = ''
nis4 = ''
mf = ['M', 'n', 'F', 'f']
for p in range(1, 5):
    print('=' * 5, f'{p}ª PESSOA', '=' * 5)
    nome = input(f'Nome: ')
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper()
    if sexo == 'M':
        masc += 1
    if sexo == 'M' or sexo == 'F':
        if p == 1:
            nis1 = [nome, idade, sexo]
            if nis1[2] == 'F' and nis1[1] < 20:
                femi += 1

        if p == 2:
            nis2 = [nome, idade, sexo]
            if nis2[2] == 'F' and nis2[1] < 20:
                femi += 1

        if p == 3:
            nis3 = [nome, idade, sexo]
            if nis3[2] == 'F' and nis3[1] < 20:
                femi += 1

        if p == 4:
            nis4 = [nome, idade, sexo]
            if nis4[2] == 'F' and nis4[1] < 20:
                femi += 1
    else:
        print('Escolha M (masculino) ou F (femimino).')
        exit('Erro de reconhecimento do sexo')
    if sexo == 'M':
        masc += 1
        if idade > hvelho:
            hvelho = idade

mi = (nis1[1] + nis2[1] + nis3[1] + nis4[1]) / 4
print(f'{mi:.0f} é a média de idade das 4 pessoas.')

if hvelho == nis1[1]:
    print(f'{nis1[0]} é o homem mais velho, com {hvelho} anos.')
elif hvelho == nis2[1]:
    print(f'{nis2[0]} é o homem mais velho, com {hvelho} anos.')
elif hvelho == nis3[1]:
    print(f'{nis3[0]} é o homem mais velho, com {hvelho} anos.')
elif hvelho == nis4[1]:
    print(f'{nis4[0]} é o homem mais velho, com {hvelho} anos.')

if femi >= 2:
    print(f'Existem {femi} mulheres que possuem menos de 20 anos.')
elif femi == 1:
    print(f'Existe apenas 1 mulher com menos de 20 anos.')
elif femi == 0:
    print('Não existe nenhuma mulher com menos de 20 anos entre os 4.')
