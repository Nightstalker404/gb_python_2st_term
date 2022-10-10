## Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# файл1: 2x^2 + 7x + 5
# файл2: 4x^2 + 3x + 9
# результат: 6x^2 + 10x + 14
lst_1 = ['2x^2', '7x', '5']
lst_2 = ['5x^2', '3x', '8']
for k, i in enumerate(lst_1):
    for j in lst_2:
        if i.count('x') == 1 and i[i.index('x'):] in j:
            lst_1[k] = str(int(i[:i.index('x')]) + int(j[:j.index('x')])) + i[i.index('x'):]
            lst_2.remove(j)
        elif i.count('x') == 0 and j.count('x') == 0:
            lst_1[k] = str(int(i) + int(j))
print(f"{' + '.join(lst_1)} = 0")