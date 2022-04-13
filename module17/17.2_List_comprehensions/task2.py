phrase = str(input('Введите строку: '))
add_sym = str(input('Введите дополнительный символ: '))

double_element_list = list((x * 2 + add_sym) for x in phrase)
print(double_element_list)