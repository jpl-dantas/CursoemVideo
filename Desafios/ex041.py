from datetime import date
ann = int(input('Em que ano você nasceu? '))
idd = date.today().year - ann
if idd <= 9:
    print('Você é classificado como um nadador mirim.')
elif 10 <= idd <= 14:
    print('Você é classificado como um nadador infantil.')
elif 15 <= idd <= 19:
    print('Você é classificado como um nadador junior.')
elif idd == 20:
    print('Você é classificado como um nadador sênior.')
elif idd > 20:
    print('Você é classificado como um nadador master')
