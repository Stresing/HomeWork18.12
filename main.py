import math


def find_farthest_orbit(list_of_orbits):  # для первой задачи
    square_orbits = []
    a = 0
    max_square = 0
    found_index = 0
    for i in list_of_orbits:
        if i[0] != i[1]:
            square_orbits.append((math.pi * max(i) * min(i)))
            if max_square < max(square_orbits):
                max_square = max(square_orbits)
                found_index = a
        a += 1
    return list_of_orbits[found_index]


characteristic=lambda x: x % 2   # для второй задачи


def same_by(operation, objects: list):  # для второй задачи
    for i in objects:
        if operation(i) == 0:
            check = True
        else:
            check = False
    if check:
        return print('same')
    else:
        return print('different')


operation_multiply = lambda x, y: x * y

operation_sum = lambda x, y: x + y

operation_extent = lambda x, y: x ** y


def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_columns + 1):
        row = []
        for j in range(1, num_rows + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(operation(i, j))
        print('\t'.join([str(i) for i in row]))
    print('\n')


def task1():
    oribts = [(1, 3), (2.5, 10,), (7, 2), (6, 6), (4, 3)]
    print(find_farthest_orbit(oribts))


def task2():
    value = list(map(int, input('Введите список через пробел: ').split()))
    same_by(characteristic, value)


def task3():
    print_operation_table(operation_multiply)
    print_operation_table(operation_sum)
    print_operation_table(operation_extent)


task = int(input("какую задачу хотите проверить ? (1-3): "))
if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
