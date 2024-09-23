num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(-1)
if 5 in num:
    num.remove(5)
else:
    print('O número 5 não esta na lista')
print(f'Essa lista possui {len(num)} elementos')
print(num)
