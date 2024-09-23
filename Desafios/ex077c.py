lista = ('abobora', 'banana', 'melancia', 'uva', 'abacaxi', 'jaca', 'goiaba', 'manga', 'pera', 'goiaba', 'kiwi')

for p in lista:
    print(f'\nNa palavra {p.upper()} existem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
