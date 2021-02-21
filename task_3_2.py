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


def num_translate_adv(key):
    new_key = key.lower()
    if new_key in numbers:
        if key.istitle():
            value = numbers.get(new_key)
            return value.title()
        else:
            value = numbers.get(new_key)
            return value
    else:
        return None


print(num_translate_adv('one'))
print(num_translate_adv('Two'))
print(num_translate_adv('Three'))
print(num_translate_adv('twelve'))
