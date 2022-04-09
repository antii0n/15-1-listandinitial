s = str(input('Введите строку: '))
index = int(input('Введите номер символа: '))

print(f'Символ слева: {s[index-2]}  Символ справа: {s[index]}')

if s.count(s[index-1])>1:
    print('Еще таких символов в строке:', s.count(s[index-1]) - 1)
else:
    print('Больше таких символов нет.')