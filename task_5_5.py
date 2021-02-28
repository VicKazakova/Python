src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# 1 способ
numbers = [elem for elem in src if src.count(elem) == 1]
print(numbers)

# 2 способ
unique_numbers = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_numbers.add(el)
    else:
        unique_numbers.discard(el)
    tmp.add(el)
unique_numbers_ver_2 = [el for el in src if el in unique_numbers]
print(unique_numbers_ver_2)
