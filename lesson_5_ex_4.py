# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def encrypt(text):
    new_text = ''
    count = 1
    for i in range(len(text) - 1):
        if i == len(text) - 2:
            new_text += f'{count + 1}{text[i]}'
        elif text[i] == text[i + 1]:
            count += 1
        else:
            new_text += f'{count}{text[i]}'
            count = 1
    return new_text


def decrypt(new_text):
    decrypt_text = ''
    num_list = ''
    alpha_list = []
    for i, v in enumerate(new_text):
        if v.isdigit():
            num_list += v
        else:
            decrypt_text += f'{v * int(num_list)}'
            num_list = ''
    return decrypt_text


print(encrypt(text))
t = encrypt(text)
print(decrypt(t))

