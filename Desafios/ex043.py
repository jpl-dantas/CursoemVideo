print('Calculo do IMC')
al = float(input('Digite a sua altura: '))
pe = float(input('Digite o seu peso: '))
imc = pe / (al * al)
print(f'IMC = {imc:.2f}')
if imc < 18.5:
    print('Você esta abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você esta no peso ideal.')
elif 25.1 <= imc <= 30:
    print('Você esta acima do peso.')
elif 30.1 <= imc <= 40:
    print('Você esta obeso.')
elif imc > 40:
    print('Você tem obesidade morbida.')
