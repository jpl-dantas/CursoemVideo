from time import sleep


def linha(a):
    print(f'{a}' * 50)


def maior(* num):
    linha("=-")
    print('Analisando os valores passados...')
    sleep(1.5)
    print('Os números:', end=' ')
    for n in num:
        print(n, end=' ')
        sleep(0.35)
    nup = len(num)
    if len(num) == 0:
        nup = 0
        mai = 0
    else:
        mai = max(num)
    print('foram passados.', end=' ')
    print(f'Ao todo foram {nup} números.')
    sleep(1)
    print(f'O maior valor informado foi {mai}.')
    sleep(1.5)


maior(12, 4, 2, 6, 7, 4, 11)
maior(5, 6, 3, 2, 9)
maior(2, 6)
maior()
