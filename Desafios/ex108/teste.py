import moeda

p = float(input('Digite o preço: R$'))
print('')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O acréscimo de 10% de {p} fica: R${moeda.aumentar(p, 10)}')
print(f'O desconto de 13% de {p} fica: R${moeda.diminuir(p, 13)}')
