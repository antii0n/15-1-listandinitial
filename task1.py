numbers = [3,7,5]
while True:
 number = int(input('Новое число: '))
 numbers.append(number)
 print('Текущий список чисел:', numbers)
 for i in numbers:
  # i = int(i)
  # print(i)
  print(i ** 2, i ** 3, i ** 4)
 print()