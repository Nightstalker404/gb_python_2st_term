# 4.	Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def show_points_coords(number: int) -> None:
    if number == 1:
        print('x > 0 и y > 0')
    elif number == 2:
        print('x < 0 и y > 0')
    elif number == 3:
        print('x < 0 и y < 0')
    elif number == 4:
        print('x > 0 and y < 0')


number = int(input('Введите номер четверти плоскости: '))
show_points_coords(number)