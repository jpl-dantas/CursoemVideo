brasil = []
estado = {}
for r in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ').upper()
    brasil.append(estado.copy())
for e in brasil:
    print(f'{e["uf"]} = {e["sigla"]}')
