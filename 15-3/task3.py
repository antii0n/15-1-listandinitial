word_list = []
for i in range(3):
    print(f'Введите {i+1} слово:', end='')
    word = str(input())
    word_list.append(word)

print('Введите текст:\n', end='>')
text = str(input())

for ind in range(3):
    print(f'{word_list[ind]}: {text.count(word_list[ind])} раз')