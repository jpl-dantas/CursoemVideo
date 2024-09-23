sal = float(input('Digite o valor do seu salário: '))
if sal >= 1250.00:
    aum = (sal / 100) * 10 + sal
    print(f'Seu salário obteve um aumento de 10% e agora você receberá R${aum:.2f} por mês.')
if sal <= 1249.99:
    aum = (sal / 100) * 15 + sal
    print(f'Seu salário obeteve um aumento de 15% e agora você receberá R${aum} por mês.')
