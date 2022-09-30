# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def digits_sum(number: float) -> int:
    return sum([int(i) for i in str(number) if i.isdigit()])


number = float(input('Введите вещественное число: '))
print(digits_sum(number))
