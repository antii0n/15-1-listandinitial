import random
from random import randint

dog_count = int(input('Введите количество собак: '))
point_list = []
for d in range(dog_count):
    point = randint(1, 100)
    print(f'У {d+1} собаки {point} очков')
    point_list.append(point)
print('Список до сортировки:', point_list)

maxmin = sorted(point_list)
point_sort = []
for i in range(dog_count):
    if point_list[i] == maxmin[0]:
        point_sort.append(maxmin[dog_count-1])
    elif point_list[i] == maxmin[dog_count-1]:
        point_sort.append(maxmin[0])
    else:
        point_sort.append(point_list[i])
print(point_sort)
