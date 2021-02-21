numbers = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"}


def num_translate(key):
    if key in numbers:
        value = numbers.get(key)
        return value
    else:
        return None


print(num_translate("one"))
print(num_translate("two"))
print(num_translate("three"))
print(num_translate("eleven"))
