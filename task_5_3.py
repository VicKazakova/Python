from itertools import zip_longest
t = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анна'
]
c = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


tutor_class = zip_longest(t, c, fillvalue=None)
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
print(next(tutor_class))
