nums = [[], [], []]
par = 0
for con in range(0, 3):
    for anl in range(0, 3):
        if con == 0:
            nums[0].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
        elif con == 1:
            nums[1].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
        elif con == 2:
            nums[2].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
        if nums[con][anl] % 2 == 0:
            par += nums[con][anl]
maxseg = max(nums[1])
print('-' * 43)

print(f'[{nums[0][0]: ^3}][{nums[0][1]: ^3}][{nums[0][2]: ^3}]')
print(f'[{nums[1][0]: ^3}][{nums[1][1]: ^3}][{nums[1][2]: ^3}]')
print(f'[{nums[2][0]: ^3}][{nums[2][1]: ^3}][{nums[2][2]: ^3}]')
print('-' * 43)

print(f'Soma dos números pares: {par}')
print(f'Soma dos valores da terceira coluna: {nums[0][2] + nums[1][2] + nums[2][2]}')
print(f'Maior valor da segunda linha: {maxseg}')
