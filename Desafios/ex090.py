aluno = {'nome': input('Nome do aluno: '), 'média': float(input('Média do aluno: '))}
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print('=' * 30)

for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')
