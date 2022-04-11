import itertools
import random
from random import randint

pack_am = int(input('Введите количество пакетов: '))

byte_general = []
for p in range(pack_am):
    print(f'Пакет номер {p}')
    byte_list = []
    for b in range(4):
        byte = randint(-1, 1)
        print(f'{b+1} бит: {byte}')
        byte_list.append(byte)
    byte_general.append(byte_list)
print(byte_general)

el_delete = []
for bl in byte_general:
    if bl.count(-1) > 1:
        print(f'Много ошибок в пакете {byte_general.index(bl)+1}')
        el_delete.append(bl)
print('Элементы на удаление:', el_delete)

for el in el_delete:
    byte_general.remove(el)
smooth_list = list(itertools.chain(*byte_general))
print("Список после удалений:", smooth_list)
print('Количество ошибок в сообщении:', smooth_list.count(-1))
print('Количество потерянных пакетов:', len(el_delete))