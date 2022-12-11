def swap(list):
    list[s1][s2] = 1


def chek(list):
    if list[1][1] == 0:
        list[1][1] = 2
    elif list[0][0] == 0:
        list[0][0] = 2
    elif list[2][2] == 0:
        list[2][2] = 2
    elif list[0][2] == 0:
        list[0][2] = 2
    elif list[2][0] == 0:
        list[2][0] = 2


def redact_indx(x):
    if x == 1:
        x = 0
    elif x == 2:
        x = 1
    elif x == 3:
        x = 2
    return x


two_list = [[1, 1, 1], [1, 1, 1], [0, 0, 1]]

xy = list(map(int, input().split()))

s1 = redact_indx(xy[0])
s2 = redact_indx(xy[1])

swap(two_list)
chek(two_list)

for i in range(len(two_list)):
    print(two_list[i])
    if i > 3:
        print('\n')
