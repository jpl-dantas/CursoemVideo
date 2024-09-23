def dobra(lis):
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1


num = [1, 4, 3, 8, 9, 2]
print(f'Antes: {num}')

dobra(num)
print(f'Depois: {num}')
