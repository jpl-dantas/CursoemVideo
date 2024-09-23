pessoas = []
dados = []
qp = 0
r = ''
while True:
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    qp += 1
    while r != 'S' and r != 'N':
        r = input('Você quer continuar? [S/N]: ').upper()
        if r == 'N' or r == 'S':
            break
        else:
            print('Por favor digite uma resposta válida')
    dados.clear()
    if r == 'N':
        print('-' * 43)
        break
    r = ''
    print('-' * 43)
if qp > 1:
    print(f'No total foram {qp} pessoas cadastradas.')
else:
    print(f'Você cadastrou apenas uma pessoa.')

peso = []
for d in pessoas:
    peso.append(d[1])
pesosp = max(peso)
pesosl = min(peso)

nome100 = []
for d in pessoas:
    if d[1] >= 100:
        nome100.append(d[0])
nome70 = []
for d in pessoas:
    if d[1] <= 70:
        nome70.append(d[0])

pma100 = 'Não teve uma pessoa de 100kg pra cima'
if pesosp >= 100:
    pma100 = f'As pessoas de 100kg pra cima são: {nome100}.'
pme70 = 'Não teve uma pessoa de 70kg pra baixo'
if pesosl <= 70:
    pme70 = f'As pessoas de 70kg pra baixo são: {nome70}.'

if len(pessoas) > 1:
    print(f'Maior peso registrado foi de {pesosp}kg | {pma100}.')
    print(f'Menor peso registrado foi de {pesosl}kg | {pme70}')
else:
    print(f'O único peso registrado foi {peso[0]}kg\n'
          f'{pma100} | {pme70}')
