nums = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
print(f'Os números pares digitados foram: {sorted(nums[0])}')
print(f'Os números ímapares digitados foram: {sorted(nums[1])}')
