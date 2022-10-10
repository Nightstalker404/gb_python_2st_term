# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())
lst = []
for i in range(2, n):
    while n % i == 0:
        lst.append(i)
        n /= i
print('Простое число' if not lst else lst)