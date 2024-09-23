palavras = ('Cachorro', 'Pipa', 'Avião', 'Baleia')
print(palavras.index('Pipa'))

for cont in range(0, len(palavras)):
    print(palavras[cont])
print(sorted(palavras))

del palavras

a = (1, 4, 6, 7)
b = (2, 6, 8, 10)
c = a + b
d = b + a
print(c)
print(d)
print(c.index(10))
