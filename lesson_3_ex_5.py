# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input())
fib = [0, 1]
for i in range(len(fib)):
    while num > 1:
        fib.append(fib[-1] + fib[-2])
        num -= 1
for i in range(len(fib) - 1):
    # while num > 0:
    fib.insert(0, (fib[1] - fib[0]))
        # num -= 1
print(fib)
