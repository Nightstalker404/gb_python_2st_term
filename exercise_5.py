# 5.	Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.

def find_distance(x1: int, y1: int, x2: int, y2: int) -> None:
    distance = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 2)
    print(distance)


x1, y1 = map(int, input('Введите координаты точки А: ').split())
x2, y2 = map(int, input('Введите координаты точки В: ').split())
find_distance(x1, y1, x2, y2)