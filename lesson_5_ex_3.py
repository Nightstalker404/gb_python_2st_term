# Создайте программу для игры в ""Крестики-нолики"".

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
# Вложенный список со всеми возможными победными комбинациями для поля любой размерности
win_combo_vertical = [[game[j][i] for j in range(len(game[i]))] for i in range(len(game))]
win_combo_diagonal = [game[i][j] for i in range(len(game)) for j in range(i, i + 1)]
win_combo_diagonal2 = [game[i][j] for i in reversed(range(len(game))) for j in range(i, i + 1)]
total_win_combo = game + win_combo_vertical + [win_combo_diagonal] + [win_combo_diagonal2]


# Функция для отображения игрового поля
def show_field():
    for i in range(len(game)):
        for j in range(len(game)):
            print(game[i][j], end=' ')
        print()

# Алгоритм хода 1 игрока
def player1():
    try:
        n = True
        while n:
            step1 = list(map(int, input('Ход 1 игрока: ').split()))
            if game[step1[0]][step1[1]] == 0:
                game[step1[0]][step1[1]] = 1
                n = False
                show_field()
            else:
                print('Ячейка занята. Введите повторно.')
    except IndexError:
        print(f'Ячейка не существует. Введите повторно число от 0 до {len(game[0]) - 1}.')
        player1()

# Алгоритм 2 игрока
def player2():
    try:
        n = True
        while n:
            step1 = list(map(int, input('Ход 2 игрока: ').split()))
            if game[step1[0]][step1[1]] == 0:
                game[step1[0]][step1[1]] = 2
                n = False
                show_field()
            else:
                print('Ячейка занята. Введите повторно.')
    except IndexError:
        print(f'Ячейка существует. Введите повторно число от 0 до {len(game[0]) - 1}.')
        player2()

# Алгоритм проверки победы игрока
def victory():
    for i in total_win_combo:
        if i.count(1) == len(i):
            return 'Игрок 1 одержал победу'
        elif i.count(2) == len(i):
            return 'Игрок 2 одержал победу'

# Игровой режим
def play():
    while True:
        player1()
        victory()
        if isinstance(victory(), str):
            return victory()
        player2()
        victory()
        if isinstance(victory(), str):
            return victory()


print(play())


