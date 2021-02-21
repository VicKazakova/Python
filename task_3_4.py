# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя
# Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по
# схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например: >>>
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева") { "А": { "П": ["Петр
# Алексеев"] }, "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } } Как поступить,
# если потребуется сортировка по ключам?
def thesaurus_adv(*args):
    employees = {}
    for people in args:
        name, surname = people.split()
        key = employees.get(surname[0])
        if key is None:
            key = {}
        full_name = key.get(name[0])
        if full_name is None:
            full_name = []
        full_name.append(people)
        key.setdefault(name[0], full_name)
        employees.setdefault(surname[0], key)
    return employees


print(thesaurus_adv("Елена Пяткина", "Раиса Петрова", "Елизавета Казакова", "Борис Короткин", "Андрей Скриба"))
