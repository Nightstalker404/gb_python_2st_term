# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def count_numbers(number: int) -> list:
    lst = []
    count = 1
    for i in range(1, number+1):
        count *= i
        lst.append(count)
    return lst


number = int(input('Введите целое число: '))
print(count_numbers(number))
