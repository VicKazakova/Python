n = int(input("Введите число n: "))
odd_number = (number for number in range(1, n + 1, 2))
print(list(odd_number))
