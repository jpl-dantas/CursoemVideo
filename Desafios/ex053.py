frase = input('Digite alguma coisa sem acentuação: ').upper()
simp = frase.split()
simp = ''.join(simp).strip()
reverso = simp[::-1]
if simp == reverso:
    print(f'O que você escreveu "{frase}" é palíndromo.')
else:
    print(f'O que você escreveu "{frase}" não é palíndromo.')
print(f'O contrário de "{frase}" é "{reverso}".')
