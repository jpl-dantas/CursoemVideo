nums = [[], [], []]
for con in range(0, 3):
    for anl in range(0, 3):
        if con == 0:
            nums[0].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
        elif con == 1:
            nums[1].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
        elif con == 2:
            nums[2].append(int(input(f'Digite um número para a posição [{con}, {anl}]: ')))
print('-' * 43)

print(f'[{nums[0][0]: ^3}][{nums[0][1]: ^3}][{nums[0][2]: ^3}]')
print(f'[{nums[1][0]: ^3}][{nums[1][1]: ^3}][{nums[1][2]: ^3}]')
print(f'[{nums[2][0]: ^3}][{nums[2][1]: ^3}][{nums[2][2]: ^3}]')
