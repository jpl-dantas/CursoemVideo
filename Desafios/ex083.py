while True:
    exp = input('Digite uma expressão com parênteses: ')
    if '(' in exp or ')' in exp:
        break
    else:
        print('Você não adicionou nenhum parêntese | Tente novamente.')
paren = []
for ele in exp:
    if ele == '(':
        paren.append('(')
    elif ele == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')
