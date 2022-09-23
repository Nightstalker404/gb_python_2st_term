# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

def find_dimension(x: int, y: int) -> None:
    if x > 0 and y > 0:
        print('I четверть плоскости')
    elif x < 0 and y > 0:
        print('II четверть плоскости')
    elif x < 0 and y < 0:
        print('III четверть плоскости')
    else:
        print('IV четверть плоскости')


x, y = map(int, input('Введите координаты x и у: ').split())
find_dimension(x, y)