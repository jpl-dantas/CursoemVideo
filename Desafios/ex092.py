from datetime import datetime

dados = {
    'nome': input('Nome da pessoa: '),
    'ano de nascimento': int(input('Ano de nascimento: ')),
    'idade': '',
    'CTPS': int(input('Carteira de trabalho (0 = não possui): '))
}

if dados['CTPS'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    idade = datetime.now().year - dados['ano de nascimento']
    dados['idade'] = idade
    tt = (dados['ano de contratação'] + 35) - datetime.now().year
    dados['aposentadoria'] = tt + idade
    print('=' * 45)
    del dados['ano de nascimento']
    for k, v in dados.items():
        print(f'{k.capitalize()}: {v}')
    print('=' * 45)
else:
    print('=' * 45)
    idade = datetime.now().year - dados['ano de nascimento']
    dados['idade'] = idade
    del dados['ano de nascimento']
    for k, v in dados.items():
        print(f'{k.capitalize()}: {v}')
    print('=' * 45)
