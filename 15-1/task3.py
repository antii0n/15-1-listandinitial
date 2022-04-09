worker_count = int(input('Введите количество сотрудников: '))
id_list = list()
for _ in range(worker_count):
    id_worker = int(input('ID сотрудника: '))
    id_list.append(id_worker)
id_search = int(input('Какой ID ищем? '))
if id_search in id_list:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает')
