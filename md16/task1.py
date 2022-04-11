zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
zoo.remove('elephant')
print(zoo)
print(f'Лев сидит в клетке №{zoo.index("lion") + 1}')
print(f'Обезьяна сидит в клетке №{zoo.index("monkey") + 1}')