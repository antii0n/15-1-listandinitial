import random

n_list = [random.randint(-20, 20) for _ in range(10)]
l_lim = random.randint(0, 7)
r_lim = random.randint(l_lim+1, 10-l_lim)
print(n_list, '\nL -', l_lim, '   R -', r_lim)
print(n_list[:l_lim] + n_list[r_lim:])