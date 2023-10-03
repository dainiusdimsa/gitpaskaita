from copy import deepcopy
countries = {
    'LT': 'Lithuania',
    'BY': 'Belarus',
    'USA': "United States",
}

print(countries.get('ES', None))

data = [1, 2, 3, 4, 1, 5]

result = {1: 0, 2: 1, 3: 2, 4: 3, 5: 5}
for index, d in enumerate([1, 3, 9]):
    result.setdefault(d, 'None')

print(result)
a = [1, 2, 3]

print(result.keys())
print(result.values())
print(result.items())

result[11] = a
# result_1 = result
result_1 = deepcopy(result)
# result_1[11] = a

# result[10] = 'ten'

a.append(10)

print(result, id(result))
print(result_1, id(result_1))
