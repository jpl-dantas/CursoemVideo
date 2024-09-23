import random
a1 = input('Escreva o nome de um dos alunos que você quer sortear: ')
a2 = input('Escreva o nome do segundo: ')
a3 = input('Agora o terceiro: ')
a4 = input('E por último o quarto: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
lista = ', '.join(lista)
print(f'A ordem de apresentação dos alunos será: {lista}')
