pessoas = []
dados = {'nome': '',
         'sexo': '',
         'idade': 0}

r = ''
while True:
    dados['nome'] = input('Nome da pessoa: ')
    while True:
        sx = input('Sexo da pessoa [M/F]: ').upper()
        if sx in 'MF':
            dados['sexo'] = sx
            break
        else:
            print('\033[31m| Por favor, digite M para Masculino ou F para Feminino.\033[m')
    dados['idade'] = int(input('Idade da pessoa: '))
    pessoas.append(dados.copy())
    print('-' * 50)
    while True:
        r = input('Você quer adicionar mais pessoas? [S/N]: ').upper()
        if r == 'N' or r == 'S':
            break
        else:
            print('\033[31m| Por favor digite uma resposta válida\033[m')
            print('-=' * 25)
    if r == 'N':
        break
print('=' * 50)

if len(pessoas) > 1:
    print(f'No total foram {len(pessoas)} pessoas cadastradas.')

    totidade = 0
    for p in pessoas:
        totidade += p['idade']
    print(f'A média de idade das pessoas é {totidade / len(pessoas):.1f}')

    qsf = 0
    for p in pessoas:
        if p['sexo'] == 'F':
            qsf += 1

    if qsf > 1:
        print('Nome das mulheres cadastradas: ', end='')
        for p in pessoas:
            if p['sexo'] == 'F':
                print(f'{p["nome"]}', end=', ')
        print('[FIM]')
    else:
        print('Foi cadastrada apenas uma mulher: ', end='')
        for p in pessoas:
            if p['sexo'] == 'F':
                print(f'{p["nome"]}.')

    qpam = 0
    for p in pessoas:
        if p['idade'] > totidade / len(pessoas):
            qpam += 1
    if qpam > 1:
        print('Pessoas com idade acima da média do grupo: ', end='')
        for p in pessoas:
            if p['idade'] > totidade / len(pessoas):
                print(f'{p["nome"]}', end=', ')
        print('[FIM]')
    else:
        print(f'Apenas uma pessoa tem a idade acima da média: ', end='')
        for p in pessoas:
            if p['idade'] > totidade / len(pessoas):
                print(f'{p["nome"]}.')

else:
    print('Foi cadastrada apenas uma pessoa.')
    print(f'Por ter apenas uma pessoa cadastrada, a média de idade é de {pessoas[0]["idade"]}.')
    if pessoas[0]['sexo'] == 'F':
        print(f'O nome da mulher cadastrada é {pessoas[0]["nome"]}.')
    else:
        print('A pessoa cadastrada não é uma mulher.')
    print('Não existe ninguém abaixo e acima da média de idade.')
