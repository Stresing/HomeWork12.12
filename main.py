def swap(list, round_x, round_y):
    if list[round_x][round_y] == 0:
        list[round_x][round_y] = 1
    else:
        print('Противник уже походил на данной точке')
        xy = list(map(int, input('Введите повторно: ').split()))
        reround_x = redact_indx(xy[0])
        reround_y = redact_indx(xy[1])
        swap(two_list, raound1_1, raound1_2)
        chek(two_list)
        return xy


def chek(list):
    if list[1][1] == 0:  # center
        list[1][1] = 2
    elif list[0][0] == 0:  # NW
        list[0][0] = 2
    elif list[2][2] == 0:  # SE
        list[2][2] = 2
    elif list[0][2] == 0:  # NE
        list[0][2] = 2
    elif list[2][0] == 0:  # SW
        list[2][0] = 2
    elif list[0][1] == 0:  # N
        list[0][1] = 2
    elif list[1][0] == 2:  # W
        list[1][0] = 2
    elif list[2][1] == 2:  # S
        list[2][1] = 2
    elif list[2][2] == 2:  # E
        list[2][2] = 2


def chek2(list):
    if list[0][0] == 0:  # NW
        list[0][0] = 2
    elif list[2][2] == 0:  # SE
        list[2][2] = 2
    elif list[0][2] == 0:  # NE
        list[0][2] = 2
    elif list[2][0] == 0:  # SW
        list[2][0] = 2
    elif list[0][1] == 0:  # N
        list[0][1] = 2
    elif list[1][0] == 2:  # W
        list[1][0] = 2
    elif list[2][1] == 2:  # S
        list[2][1] = 2
    elif list[2][2] == 2:  # E
        list[2][2] = 2
    # if list[1][1] and list[0][0]:  # center and NW  Попытка сделать пк умнее
    #     if list[2][2] == 0:
    #         list[2][2] = 2
    # elif list[0][0] and list[0][2] == 2:  # NW
    #     if list[0][1] == 0:
    #         list[0][1] = 2
    # elif list[2][2] and list[0][1] == 2:  # SE
    #     if list[1][2] == 0:
    #         list[1][2] = 2
    # elif list[0][2] and list[2][2] == 2:  # NE
    #     if list[1][2] == 0:
    #         list[1][2] = 2
    # elif list[2][0] and list[2][2] == 2:  # SW
    #     if list[2][1] == 0:
    #         list[2][1] = 2


def check_Win(list):
    if list[0][0] == list[1][1] == list[2][2] == 1:  # 1
        print("вы вин")
    elif list[0][2] == list[1][1] == list[2][0] == 1:  # 2
        print("вы вин")
    elif list[0][0] == list[0][1] == list[0][2] == 1:  # 3
        print("вы вин")
    elif list[1][0] == list[1][1] == list[1][2] == 1:  # 4
        print("вы вин")
    elif list[2][0] == list[2][1] == list[2][2] == 1:  # 5
        print("вы вин")
    elif list[0][0] == list[1][0] == list[2][0] == 1:  # 6
        print("вы вин")
    elif list[0][1] == list[1][1] == list[2][1] == 1:  # 7
        print("вы вин")
    elif list[0][2] == list[1][2] == list[2][2] == 1:  # 8
        print("вы проиграли")
    if list[0][0] == list[1][1] == list[2][2] == 2:  # 1
        print("вы проиграли")
    elif list[0][2] == list[1][1] == list[2][0] == 2:  # 2
        print("вы проиграли")
    elif list[0][0] == list[0][1] == list[0][2] == 2:  # 3
        print("вы проиграли")
    elif list[1][0] == list[1][1] == list[1][2] == 2:  # 4
        print("вы проиграли")
    elif list[2][0] == list[2][1] == list[2][2] == 2:  # 5
        print("вы проиграли")
    elif list[0][0] == list[1][0] == list[2][0] == 2:  # 6
        print("вы проиграли")
    elif list[0][1] == list[1][1] == list[2][1] == 2:  # 7
        print("вы проиграли")
    elif list[0][2] == list[1][2] == list[2][2] == 2:  # 8
        print("вы проиграли")


def redact_indx(x):
    if x == 1:
        x = 0
    elif x == 2:
        x = 1
    elif x == 3:
        x = 2
    return x


def task2():
    two_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    xy = list(map(int, input('Введите позицию вашего хода (индексация идёт с 1 до 3 например"1 3" будет первая строка 3ий столбец').split()))
    raound1_1 = redact_indx(xy[0])
    raound1_2 = redact_indx(xy[1])
    swap(two_list, raound1_1, raound1_2)
    chek(two_list)
    check_Win(two_list)

    for i in range(len(two_list)):
        print(two_list[i])
        if i > 3:
            print('\n')

    xy = list(map(int, input().split()))
    raound2_1 = redact_indx(xy[0])
    raound2_2 = redact_indx(xy[1])
    swap(two_list, raound2_1, raound2_2)
    chek2(two_list)
    check_Win(two_list)

    for i in range(len(two_list)):
        print(two_list[i])
        if i > 3:
            print('\n')

    xy = list(map(int, input().split()))
    raound3_1 = redact_indx(xy[0])
    raound3_2 = redact_indx(xy[1])
    swap(two_list, raound3_1, raound3_2)
    chek2(two_list)
    check_Win(two_list)

    for i in range(len(two_list)):
        print(two_list[i])
        if i > 3:
            print('\n')

    xy = list(map(int, input().split()))
    raound4_1 = redact_indx(xy[0])
    raound4_2 = redact_indx(xy[1])
    swap(two_list, raound4_1, raound4_2)
    chek2(two_list)
    check_Win(two_list)

    for i in range(len(two_list)):
        print(two_list[i])
        if i > 3:
            print('\n')


def task1():
    s = input('Введите строку: ').split()
    print(' '.join(
        filter(lambda x: x not in ["АБВ", "абв"], s)))  # Некий текст содержащий различные буквы в том числе АБВ и абв


def task3():
    def press(file, result):
        with open(file, 'r', encoding='utf-8') as text:
            with open(result, 'w', encoding='utf-8') as res:
                inp_str = text.readline()
                ind = 0
                count = 1
                while ind < len(inp_str) - 1:
                    if inp_str[ind] == inp_str[ind + 1]:
                        count += 1
                    else:
                        if count == 1:
                            res.write(inp_str[ind])
                        else:
                            res.write(str(count) + inp_str[ind])
                        count = 1
                    ind += 1

    def depress(file, result):
        with open(file, 'r', encoding='utf-8') as text:
            with open(result, 'w', encoding='utf-8') as res:
                inp_str = text.readline()
                count = ''
                for letter in inp_str:
                    if letter.isdigit():
                        count += letter
                    else:
                        if not count:
                            res.write(int(count) * letter)
                        else:
                            res.write(letter)
                        count = ''

    press('file.txt', 'result.txt')
    depress('result.txt', 'result2.txt')


task = int(input("Какую задачу хотите проверить?"))
if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
