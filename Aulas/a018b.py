pessoas = [['Maria', 16], ['Davi', 27], ['João', 15], ['Mateus', 11]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')
print('-' * 30)

galera = []
dados = []
for c in range(0, 3):
    dados.append(input('Digite um nome: '))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
print('-' * 30)
tome = toma = 0
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade.')
        toma += 1
    else:
        print(f'{p[0]} é menor de idade')
        tome += 1
print(f'Existem {toma} pessoas maiores de idade e {tome} menores de idade.')
