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
    if list[1][1] and list[0][0]: # center and NW
        if list[2][2]  == 0:
            list[2][2] = 2
    elif list[0][0] and list[0][2] == 2:  # NW
        if list[0][1] == 0:
            list[0][1] = 2
    elif list[2][2] and list[0][1] == 2:  # SE
        if list[1][2] == 0:
            list[1][2] = 2
    elif list[0][2] and list[2][2] == 2:  # NE
            if list[1][2] == 0:
                list[1][2] = 2
    elif list[2][0] and list[2][2] == 2:  # SW
            if list[2][1] == 0:
                list[2][1] = 2
    #     list[2][0] = 2
    # elif list[0][1] == 0:  # N
    #     list[0][1] = 2
    # elif list[1][0] == 2:  # W
    #     list[1][0] = 2
    # elif list[2][1] == 2:  # S
    #     list[2][1] = 2
    # elif list[2][2] == 2:  # E
    #     list[2][2] = 2

def redact_indx(x):
    if x == 1:
        x = 0
    elif x == 2:
        x = 1
    elif x == 3:
        x = 2
    return x


two_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

xy = list(map(int, input().split()))
raound1_1 = redact_indx(xy[0])
raound1_2 = redact_indx(xy[1])
swap(two_list, raound1_1, raound1_2)
chek(two_list)

for i in range(len(two_list)):
    print(two_list[i])
    if i > 3:
        print('\n')

xy = list(map(int, input().split()))
raound2_1 = redact_indx(xy[0])
raound2_2 = redact_indx(xy[1])
swap(two_list, raound2_1, raound2_2)
chek2(two_list)

for i in range(len(two_list)):
    print(two_list[i])
    if i > 3:
        print('\n')

xy = list(map(int, input().split()))
raound3_1 = redact_indx(xy[0])
raound3_2 = redact_indx(xy[1])
swap(two_list, raound3_1, raound3_2)
chek2(two_list)

for i in range(len(two_list)):
    print(two_list[i])
    if i > 3:
        print('\n')

xy = list(map(int, input().split()))
raound4_1 = redact_indx(xy[0])
raound4_2 = redact_indx(xy[1])
swap(two_list, raound4_1, raound4_2)
chek2(two_list)

for i in range(len(two_list)):
    print(two_list[i])
    if i > 3:
        print('\n')