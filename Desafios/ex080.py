nums = []
for n in range(0, 5):
    nu = int(input('Digite um número: '))
    if n == 0 or nu > nums[-1]:
        nums.append(nu)
        print('Número colocado no final da lista.')
    else:
        pos = 0
        while pos < len(nums):
            if nu <= nums[pos]:
                nums.insert(pos, nu)
                print(f'Número colocado na posição {pos}')
                break
            pos += 1
print(nums)
