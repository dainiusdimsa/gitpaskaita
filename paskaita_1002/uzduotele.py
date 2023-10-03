# List comprehention. Parasyti funkcija, kurioje varable butu iterable tipas. Ir
# reikia suskaiciuo skaiciu besidalinanciu is 3 suma.

data_list = [3, 6, 9, 12, 171, 97, 912, 686, 94, 156, 71, 260, 275, 86, 612, 80, 923,
             346, 337, 278, 108, 856, 397, 829]


# Ar set iterable???
data_set = {3, 6, 9, 12, 171, 97, 912, 686, 94, 156, 71, 260, 275, 86, 612, 80, 923,
            346, 337, 278, 108, 856, 397, 829}


def sum_by_3(data):
    return sum([d for d in data if d % 3 == 0])


print(sum_by_3(data_list))
print(sum_by_3(data_set))


data_dict = {1: 3, 2: 6, 3: 9, 4: 12, 5: 171, 6: 97, 7: 912, 8: 686, 9: 94, 10: 156,
             11: 71, 12: 260, 13: 912, 14: 171, 15: 156, 16: 612, 17: 108}

# print(sum_by_3(data_dict))