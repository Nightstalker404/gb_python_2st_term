# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

test = 'рапро выаоабв рпрабв kyuy'
print(*filter(lambda x: 'абв' not in x, test.split()))