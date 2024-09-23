from random import choice
a1 = input('Escreva o nome de um dos alunos que você quer sortear: ')
a2 = input('Escreva o nome do segundo: ')
a3 = input('Agora o terceiro: ')
a4 = input('E por último o quarto: ')
ae = choice([a1, a2, a3, a4])
print(f'O aluno escolhido foi: {ae}')
