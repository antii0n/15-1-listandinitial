q_worker = int(input('Введите количество сотрудников: '))

salary_list = []
for w in range(q_worker):
    print(f'Зарплата {w+1} сотрудника:', end=' ')
    salary = int(input())
    salary_list.append(salary)

while 0 in salary_list:
    salary_list.remove(0)

print('Осталось сотрудников:', len(salary_list))
print('Зарплаты:',salary_list)