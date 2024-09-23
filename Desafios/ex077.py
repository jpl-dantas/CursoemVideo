lista = ('abobora', 'banana', 'melancia', 'uva', 'abacaxi', 'jaca', 'goiaba', 'manga', 'pera', 'goiaba', 'kiwi')

for cont in range(0, len(lista)):
    print(f'Na palavra {lista[cont].upper()} existem as vogais: ', end='')
    if 'a' in lista[cont]:
        if 'e' in lista[cont]:
            print('a ' * lista[cont].count('a'), end='')
        elif 'i' in lista[cont]:
            print('a ' * lista[cont].count('a'), end='')
        elif 'o' in lista[cont]:
            print('a ' * lista[cont].count('a'), end='')
        elif 'u' in lista[cont]:
            print('a ' * lista[cont].count('a'), end='')
        else:
            print('a ' * lista[cont].count('a'))
    if 'e' in lista[cont]:
        if 'i' in lista[cont]:
            print('e ' * lista[cont].count('e'), end='')
        elif 'o' in lista[cont]:
            print('e ' * lista[cont].count('e'), end='')
        elif 'u' in lista[cont]:
            print('e ' * lista[cont].count('e'), end='')
        else:
            print('e ' * lista[cont].count('e'))
    if 'i' in lista[cont]:
        if 'o' in lista[cont]:
            print('i ' * lista[cont].count('i'), end='')
        elif 'u' in lista[cont]:
            print('i ' * lista[cont].count('i'), end='')
        else:
            print('i ' * lista[cont].count('i'))
    if 'o' in lista[cont]:
        if 'u' in lista[cont]:
            print('i ' * lista[cont].count('i'), end='')
        else:
            print('i ' * lista[cont].count('i'))
    if 'u' in lista[cont]:
        print('u' * lista[cont].count('u'))
