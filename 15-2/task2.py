i_list = int(input('Количество чисел в списке: '))

num_list = []
for count in range(i_list):
    print(f'Введите {count+1} число: ', end='')
    num = int(input())
    num_list.append(num)

divisor = int(input('Введите делитель: '))
summ_i = 0
for i in range(i_list):
    if num_list[i] % divisor == 0:
        print(f'Индекс числа {num_list[i]}: {i}')
        summ_i += i

print('Сумма индексов:', summ_i)