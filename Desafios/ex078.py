nums = []
for n in range(0, 5):
    nums.append(int(input(f'Digite o número na posição {n}: ')))
maxn = max(nums)
minn = min(nums)
print(f'{max(nums)} é o maior valor da lista que aparece nas posições: ', end='')
for pos, num in enumerate(nums):
    if num == maxn:
        print(f'{pos}', end='...')
print('.')
print(f'{min(nums)} é o menor valor da lista que aparece nas posições: ', end='')
for pos, num in enumerate(nums):
    if num == minn:
        print(f'{pos}', end='...')
