def leiaint(msg):
    ok = False
    valor = 0
    while not ok:
        n = str(input(msg))  # Isso faz com que a mensagem vire um input de string
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31m ERRO! | Digite um número inteiro\033[m')
    return valor


nu = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {nu}.')
