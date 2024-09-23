dic = {'João': 15, 'Cris': 41, 'Marcos': 12, 'Narciso': 36}
dic_values_ordenado = sorted(dic.items(), key=lambda value: value[1])
dic_keys_ordenado = sorted(dic.items(), key=lambda key: key[0])

print(dic_values_ordenado)
print(dic_keys_ordenado)