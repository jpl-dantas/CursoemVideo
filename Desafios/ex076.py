listagem = ('Notebook Ideapad i3 Ryzen 5 VHG 8', 2800, 'POCO M5', 1020, 'Xbox Series S', 2100,
            'Samsung Galaxy A13', 870, 'For Honor', 97.80, 'Mouse Gamer Knup KP-44', 130)

print('-' * 47)
print(f'{"LISTAGEM DE PREÇO":^47}')
print('-' * 47)

for i in range(0, len(listagem), 2):
    item = listagem[i]
    preco = listagem[i + 1]
    print(f'{item:.<40}R${preco:>5}')

print('-' * 47)
