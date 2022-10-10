# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
from itertools import zip_longest

k = int(input())
lst_k = [f'x^{i + 1}' if i != 0 else 'x' for i in reversed(range(k))]
lst = [randint(0, 100) for i in range(k+1)]
lst_3 = [f'{i}*{j}' for i, j in zip_longest(lst, lst_k, fillvalue='')]
# Используем контекстный менеджер который автоматически закрывает файл
with open('ex4.txt', 'w') as f:
    f.write(f"{' + '.join(lst_3)[:-2]} = 0")