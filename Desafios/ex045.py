import random
import time
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
maquina = random.choice([pedra, papel, tesoura])
print('-' * 5, '\033[4;35mJOKÊNPO\033[m', '-' * 5)
time.sleep(0.5)
print('\033[33m1 - Pedra')
time.sleep(0.3)
print('2 - Papel')
time.sleep(0.3)
print('3 - Tesoura\033[m')
time.sleep(0.3)
print('-' * 19)
time.sleep(0.5)
escolha = input('Qual opção você irá escolher? ').upper()
if escolha == '1' or escolha == 'PEDRA':
    escolha = pedra
elif escolha == '2' or escolha == 'PAPEL':
    escolha = papel
elif escolha == '3' or escolha == 'TESOURA':
    escolha = tesoura
else:
    print('Opção inválida.')
    exit()
time.sleep(0.5)
print('\033[1;33mPreparado?\033[m')
time.sleep(1)
print('\033[35mJo ', end='')
time.sleep(0.5)
print('Ken ', end='')
time.sleep(0.5)
print('Pô!\033[m')
time.sleep(0.5)
print('-' * 19)
time.sleep(1)
print(f'Você escolheu \033[36m{escolha.capitalize()}\033[m '
      f'e a máquina escolheu \033[31m{maquina.capitalize()}\033[m.')
if escolha == maquina:
    print('\033[33mEmpate.\033[m')
elif escolha == pedra and maquina == tesoura:
    print('\033[32mVocê venceu!\033[m')
elif escolha == pedra and maquina == papel:
    print('\033[31mVocê perdeu!\033[m')
elif escolha == papel and maquina == pedra:
    print('\033[32mVocê venceu!\033[m')
elif escolha == papel and maquina == tesoura:
    print('\033[31mVocê perdeu!\033[m')
elif escolha == tesoura and maquina == papel:
    print('\033[32mVocê venceu!\033[m')
elif escolha == tesoura and maquina == pedra:
    print('\033[31mVocê perdeu!\033[m')
