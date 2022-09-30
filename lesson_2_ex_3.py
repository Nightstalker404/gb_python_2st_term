# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def sum_formula(n: int) -> float:
    count = 0
    for i in range(1, n+1):
        count += (1+1/i) ** i
    return count


number = int(input('Введите целое число: '))
print(sum_formula(number))