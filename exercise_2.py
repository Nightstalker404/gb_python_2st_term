# 2.Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def fill_list(num):
    xyz = ["X", "Y", "Z"]
    lst = []
    for i in range(num):
        lst.append(input(f"Введите значение {xyz[i]}: "))
    return lst


def check_predict(x):
    return not (x[0] or x[1] or x[2]) == (not x[0]) and (not x[1]) and (not x[2])


lst = fill_list(3)

if check_predict(lst):
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
