# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input())
bin_num = ''

while number > 0:
    bin_num = str(number % 2) + bin_num
    number = number // 2

print(bin_num)