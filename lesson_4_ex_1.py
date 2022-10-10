# # Вычислить число c заданной точностью d
import math

d = str(float(input()))
d = len(d) - 1 - d.index('.')
print(str(math.pi)[:d + 2])  # Округление срезом
print(round(math.pi, int(d)))  # Округление встроенной функцией