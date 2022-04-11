line_1 = str(input('Первое сообщение: '))
line_2 = str(input('Второе сообщение: '))

countline1 = 0
countline2 = 0
for sym1 in line_1:
    if sym1 == '!' or sym1 == '?':
        countline1 += 1
for sym2 in line_2:
    if sym2 == '!' or sym2 == '?':
        countline2 += 1

if countline1 > countline2:
    print(line_1 + line_2)
elif countline1 < countline2:
    print(line_2 + line_1)
else:
    print('Ой')
