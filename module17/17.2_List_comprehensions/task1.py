diap_left = int(input('Левая граница: '))
diap_right = int(input('Правая граница: '))

cubic_list = list(x**3 for x in range(diap_left, diap_right+1))
quad_list = list(x**2 for x in range(diap_left, diap_right+1))
print(f'Список кубов чисел в диапазоне от '
      f'{diap_left} до {diap_right}: {cubic_list}'
      f'\nСписок квадратов чисел в диапазоне от '
      f'{diap_left} до {diap_right}: {quad_list}'
      )
