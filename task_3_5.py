from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(jokes, repeat=True):
    """
    Функция возвращает определенное число шуток, состоящих из набора слов из словарей
    :param jokes: кол-во шуток
    :param repeat: маркер, отражающий уникальность/неуникальность
    :return: случайная шутка
    """
    repeat_dict_noun = []
    repeat_dict_adv = []
    repeat_dict_adj = []
    if repeat:
        for joke in range(0, jokes):
            random_noun = choice(nouns)
            random_adverb = choice(adverbs)
            random_adj = choice(adjectives)
            joke = f'{random_noun} {random_adverb} {random_adj}'
            print(joke)
    if not repeat:
        for joke in range(0, jokes):
            random_noun = choice(nouns)
            random_adverb = choice(adverbs)
            random_adj = choice(adjectives)
            joke = f'{random_noun} {random_adverb} {random_adj}'
            print(joke)
            repeat_dict_noun.append(random_noun)
            nouns.remove(random_noun)
            repeat_dict_adv.append(random_adverb)
            adverbs.remove(random_adverb)
            repeat_dict_adj.append(random_adj)
            adjectives.remove(random_adj)
        for extra_word in repeat_dict_noun:
            nouns.append(extra_word)
        for extra_word in repeat_dict_adv:
            adverbs.append(extra_word)
        for extra_word in repeat_dict_adj:
            adjectives.append(extra_word)


get_jokes(3)
