def odd_number(max_number):
    for number in range(1, max_number + 1, 2):
        yield number


n = int(input("Введите число n: "))
print(list(odd_number(n)))
