dados = {'nome': 'Pedro', 'idade': '25'}
# Ou
dados2 = {
    'nome': 'Pedro',
    'idade': '25',
}

dados3 = {
    'nome': input('Digite o seu nome: '),
    'idade': int(input('Digite a sua idade: '))
}

print(dados['nome'], dados['idade'])
print(dados2['nome'], dados2['idade'])
print(dados3['nome'], dados3['idade'])
print('-' * 15)

print(dados.values())
print(dados.keys())
print(dados.items())
print('-' * 15)

dados['sexo'] = 'Masculino'
print(dados.items())
print('-' * 15)

del dados['idade']
print(dados.items())
print('-' * 15)

for k, v in dados.items():
    print(f'{k}: {v}')
