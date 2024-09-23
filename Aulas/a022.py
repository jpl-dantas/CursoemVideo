from Uteis import Numeros  # Importando o módulo com as funções que eu mesmo criei. Como se fosse uma biblioteca.

num = int(input('Digite um valor: '))
print(f'O número {num} elevado ao cubo é {Numeros.cubo(num)}.')
print(f'O quadrado de {num} é {Numeros.quadrado(num)}.')
print(f'O dobro de {num} é {Numeros.dobro(num)}.')
