def show_field(f):
    print(' ' + '___ ' * (size))
    for k in range(size):
        print('|' + '   |' * (size))
        line = []
        for m in range(size):
            line.append('|')
            line.append(f.get(10 * k + m))
        print(*line, '|')
        print('|' + '___|' * (size))


def keys(n=3):
    keys = set()
    key = 0
    for i in range(n + 1):
        for j in range(n + 1):
            key = j + 10 * i
            keys.add(key)
    return keys


def nums_field():
    field = {}
    for i in keys(size - 1):
        if 0 <= i < 10:
            field[i] = i
        elif 10 <= i < 100 and not i % 10:
            field[i] = i // 10
        else:
            field[i] = ' '
    return field


def step():
    while True:
        button = input('Введите № клетки (0 - выход из программы): ')
        if button != '0':
            if not button.isdigit():
                print('Только цифры. Повторите ввод № клетки ')
                continue
            button = int(button)
            if button == 0 or button < 10 or button % 10 == 0 or button % 10 > N or button // 10 > N:
                print('Запрещенный символ. Повторите ввод № клетки ')
                continue
            if field[int(button)] != ' ':
                print('Клетка занята. Повторите ввод № клетки ')
                continue
        return button


def sum_lines(mL):
    sumL = []
    LL = len(mL)

    for j in range(size - 1):
        line = []
        for i in range(size - 1):
            line.append(mL[i + j * (size - 1)])
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)
    for j in range(size - 1):
        line = []
        for i in range(size - 1):
            line.append(mL[i * (size - 1) + j])
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)
    for i in range(1, N - 1):
        var = 0
        line = []
        j = i
        while var <= N - 1 - i:
            line.append(mL[j])
            var += 1
            j += N + 1
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)
    for i in range(1, N - 1):
        var = 0
        line = []
        j = i
        while var <= i:
            line.append(mL[j])
            var += 1
            j += N - 1
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)
    for i in range(LL - 1, LL - N, -1):
        var = 0
        line = []
        j = i
        while var <= N - LL + i:
            line.append(mL[j])
            var += 1
            j = j - N - 1
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)
    for i in range(LL - 2, LL - N - 1, -1):
        var = 0
        line = []
        j = i
        while var <= LL - 1 - i:
            line.append(mL[j])
            var += 1
            j = j - N + 1
        kit = (''.join(line)).strip(' ')
        sumL.append(kit)

    return sumL


def main_field(f):
    field = f.copy()
    for i in range(size):
        field.pop(i)
        i += size
    for i in range(1, size):
        i = i * 10
        field.pop(i)
    fild_tuple = sorted(field.items(), key=lambda x: x[0])
    sort_field = dict(fild_tuple)
    line = list(sort_field.values())
    return line


def chek_winner(kL, B):
    win = None
    winO = winX = 'empty'
    for part in kL:
        kit = (''.join(part)).strip(' ')
        if kit.find('O' * R) >= 0:
            winO = 'fuLL'
        elif kit.find('X' * R) >= 0:
            winX = 'fuLL'
        if winO == 'fuLL' and winX == 'fuLL':
            win = 'Ничья'
        elif winO == 'fuLL' and winX == 'empty':
            win = 'Победил "O"'
        elif winO == 'empty' and winX == 'fuLL' and benefit:
            win = 'Победил "X"'
        elif winO == 'empty' and winX == 'fuLL' and not benefit:
            win = 'Attantion'
    return win


print(f'Правила: 1. Размер поля - высота и ширина в клетках.\n'
      f'         2. Для хода нужно без пробела вводить две цифры:\n'
      f'            первая - номер строки, вторая - столбца.\n'
      f'         3. Если размер поля от 3 до 5, игра идёт "до трёх",\n'
      f'            если 6 и более, то "до 4".\n'
      f'         4. Учитывается горинтальная, вертикальная и наклонная\n'
      f'            расстановка символов\n'
      f'         5. Первый ход выполняет "Х"\n'
      f'             УДАЧИ !!!')

N = input('Ведите размер поля (от 3 до 9): ')
while not (N.isdigit() and (3 <= int(N) <= 9)):
    N = input('Повторите ввод размера поля (от 3 до 9): ')
N = int(N)
size = N + 1
if N <= 5:
    R = 3
else:
    R = 4
field = nums_field()
button = None
count = 0
benefit = False
while button != 0:
    show_field(field)
    main_line = main_field(field)
    chek_kit = sum_lines(main_line)
    winner = chek_winner(chek_kit, benefit)
    if ' ' not in main_line and not winner:
        print('Победителей нет!')
        break
    if ' ' not in main_line and winner == 'Attantion': 
        print('Игра окончена!! Победил "X"')
        break
    if ' ' not in main_line and winner: 
        print('Игра окончена!!', winner)
        break
    
    if winner:
        if winner == 'Attantion':
            benefit = True
            print('Внимание, у "O" последний ход...')
            mark = 'O'
            count += 1
        if winner == 'Ничья':
            print('Игра окончена!!', winner, '!!')
            break
        elif winner == 'Победил "X"' or winner == 'Победил "O"':
            print('Игра окончена!!', winner, '. Поздравляю!!')
            break

    button = int(step())

    if benefit == 0:
        if count % 2:
            mark = 'O'
        else:
            mark = 'X'
    count += 1
    field[button] = mark
