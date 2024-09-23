va = 0
maiorpeso = 0
menorpeso = 0
peso = 0
for pess in range(1, 6):
    va = float(input(f'Digite o peso da {pess}ª pessoa: '))
    if pess == 1:
        maiorpeso = va
        menorpeso = va
    else:
        if va > maiorpeso:
            maiorpeso = va
        if va < menorpeso:
            menorpeso = va

print(f'A pessoa com mais peso possui {maiorpeso}kg.')
print(f'E a pessoa com menos peso possui {menorpeso}kg.')
