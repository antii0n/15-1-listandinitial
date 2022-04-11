main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

main.extend(first_company+second_company+third_company)

zero_count = 0
for i in main:
    if i == 0:
        zero_count += 1
print(f'Общий список задач: {main}\nКол-во невыполненных задач: {zero_count}')