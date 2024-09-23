def area(la, co):
    print(f'A área de um terreno com {la} de largura e {co} de comprimento é de {la * co:.1f}m².')


print(f' CONTROLE DE TERRENO ')
print('=' * 21)
lar = float(input('Digite a largura do terreno: '))
com = float(input('Digite o comprimento do terreno: '))
print('=' * 21)
area(lar, com)
