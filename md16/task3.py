films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
    'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники',
    'Деревня', 'Остров проклятых', 'Начало', 'Матрица'
]
films_top = []
print('Ваш текущий топ фильмов:', films_top)
while True:
    film_name = str(input('Название фильма: '))
    if film_name.lower() == 'пнх':
        break
    print('Команды: добавить, вставить, удалить')
    command = str(input())
    if command == 'добавить':
        films_top.append(film_name)
    elif command == 'вставить':
        place_f = int(input('На какую позицию? '))
        films_top.insert(place_f, film_name)
    elif command == 'удалить':
        if film_name in films_top:
            films_top.remove(film_name)
        else:
            print(f'Фильма "{film_name}" не было в вашем списке.')

print(set(films_top))