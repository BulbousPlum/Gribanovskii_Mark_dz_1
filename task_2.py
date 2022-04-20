# Задание A
cube_list_1 = []
for i in range(1, 1000, 2):
    cube_list_1.append(i ** 3)
num_s = 0
for i in cube_list_1:
    s_1 = 0
    n = i
    while i > 0:
        s_1 += i % 10
        i //= 10
    if s_1 % 7 == 0:
        num_s += n
print('а', '=', num_s)

# Задание B
cube_list_2 = []
for i in range(1, 1000, 2):
    cube_list_2.append(i ** 3 + 17)
num_s_2 = 0
for i in cube_list_2:
    s_2 = 0
    n_2 = i
    while i > 0:
        s_2 += i % 10
        i //= 10
    if s_2 % 7 == 0:
        num_s_2 += n_2
print('b', '=', num_s_2)
