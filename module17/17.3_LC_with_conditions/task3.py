import random

squad_1= list(random.randint(50, 80) for _ in range(10))
squad_2 = list(random.randint(30, 60) for _ in range(10))
squad_damage = list(('Погиб' if squad_1[i_damage]+squad_2[i_damage]>100
                    else 'Выжил'
                     ) for i_damage in range(10)
                    )

print(squad_damage)
