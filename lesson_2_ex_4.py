# Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def product_list(n: int, a: int, b: int) -> int:
    lst = [i for i in range(-n, n + 1)]
    position_product = lst[a] * lst[b]
    print(lst)
    return position_product


number = int(input('Введите целое число: '))
position_a = int(input('Введите начальный индекс: '))
position_b = int(input('Введите конечный индекс: '))
print(product_list(number, position_a, position_b))