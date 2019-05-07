import copy


def display(m):
    for x in range(len(m[0])):
        for y in range(len(m)):
            if y == (len(m) - 1):
                print(m[y][x])
                break
            print(m[y][x], ' ', end='')
    print('-' * len(m) * 3)


def counter(massive, x, y):
    count = 0
    if massive[y - 1][x] == 1:
        count += 1
    if massive[y + 1][x] == 1:
        count += 1
    if massive[y - 1][x - 1] == 1:
        count += 1
    if massive[y + 1][x - 1] == 1:
        count += 1
    if massive[y][x - 1] == 1:
        count += 1
    if massive[y - 1][x + 1] == 1:
        count += 1
    if massive[y + 1][x + 1] == 1:
        count += 1
    if massive[y][x + 1] == 1:
        count += 1
    return count


def check(m):
    s = copy.deepcopy(m)
    for x in range(1, len(m[0]) - 1):
        for y in range(1, len(m) - 1):
            count = counter(m, x, y)
            if m[y][x] == 0:
                if count == 3:
                    s[y][x] = 1
                    continue
            if m[y][x] == 1:
                if count < 2 or count > 3:
                    s[y][x] = 0
    return s
