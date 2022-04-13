diap_left = int(input('Введите нижнюю границу диапазона: '))
diap_right = int(input('Введите верхнюю границу диапазона: '))

sq_cubes = list(x**2 for x in range(diap_left, diap_right+1) if x % 2 == 0)
print(sq_cubes)