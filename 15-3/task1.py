s = str(input('Введите текст: '))
s_new = str()
count = 0
for sym in s:
    if sym == ':':
        s_new += ';'
        count += 1
    else:
        s_new += sym
print(f'Исправленная строка: {s_new}\nКоличество замен: {count}')
