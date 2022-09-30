# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя,
# но другие методы из библиотеки random - можно).

from random import randint, randrange


def shuffle_list(lst: list) -> list:
    return [lst.pop(randrange(0, len(lst))) for i in range(len(lst))]


lst = [i + randint(1, 5) for i in range(10)]
print(lst)  # Печатаем исходный список для наглядного сравнения
print(shuffle_list(lst))  # Печатаем перемешанный список
