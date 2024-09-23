from datetime import date
atual = date.today().year
anos = 0
a = 0
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    a = int(input(f'Qual é o ano de nascimento da {pess}ª pessoa? '))
    if atual - a >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Existem {totmaior} pessoa(s) com maior idade.')
print(f'E {totmenor} com menor idade.')
